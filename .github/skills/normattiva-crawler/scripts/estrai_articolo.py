#!/usr/bin/env python3
"""
estrai_articolo.py — Estrae il testo di un atto su Normattiva.it

Scarica localmente l'export Akoma Ntoso (XML) dell'atto e stampa a video:
  - SOLO l'articolo richiesto, se viene passato --art (risparmio di token);
  - TUTTI gli articoli dell'atto, se --art non viene passato.

Uso:
  # un solo articolo
  python estrai_articolo.py --urn "urn:nir:stato:decreto.legislativo:2024-07-12;103" --art 2
  python estrai_articolo.py --data 2024-07-18 --codice 24G00121 --art 2
  # atto completo (tutti gli articoli)
  python estrai_articolo.py --urn "urn:nir:stato:legge:2025-12-02;181"

Output: citazione + testo letterale dell'articolo richiesto o dell'intero atto.
"""
import argparse
import sys
import re
from datetime import date
from xml.etree import ElementTree as ET
import requests

BASE = "https://www.normattiva.it"
UA = {"User-Agent": "Mozilla/5.0 (compatible; law-expert/1.0)"}


def risolvi_urn(session, urn):
    """Da un URN risale a (data_pubblicazione, codice_redazionale)."""
    url = f"{BASE}/uri-res/N2Ls?{urn}"
    r = session.get(url, timeout=30)
    r.raise_for_status()
    data = re.search(r"atto\.dataPubblicazioneGazzetta=(\d{4}-\d{2}-\d{2})", r.text)
    cod = re.search(r"atto\.codiceRedazionale=([0-9A-Za-z]+)", r.text)
    if not (data and cod):
        sys.exit("ERRORE: impossibile risolvere l'URN. Verifica gli estremi dell'atto.")
    return data.group(1), cod.group(1)


def scarica_akn(session, data_pub, codice):
    """Riscalda la sessione e scarica l'XML Akoma Ntoso dell'atto."""
    # 1. la sessione deve avere l'atto in contesto
    session.get(
        f"{BASE}/atto/caricaDettaglioAtto"
        f"?atto.dataPubblicazioneGazzetta={data_pub}&atto.codiceRedazionale={codice}"
        f"&tipoDettaglio=originario&qId=",
        timeout=30,
    )
    # 2. scarica AKN (data vigenza = oggi)
    dataGU = data_pub.replace("-", "")
    data_vigenza = date.today().strftime("%Y%m%d")
    r = session.get(
        f"{BASE}/do/atto/caricaAKN?dataGU={dataGU}&codiceRedaz={codice}&dataVigenza={data_vigenza}",
        timeout=30,
    )
    r.raise_for_status()
    if "xml" not in r.headers.get("Content-Type", ""):
        sys.exit("ERRORE: l'atto non e' disponibile in formato AKN.")
    r.encoding = "utf-8"
    return r.text


def estrai_articolo(xml_text, numero):
    """Restituisce (rubrica, testo) del solo articolo richiesto, o None."""
    root = ET.fromstring(xml_text.encode("utf-8"))
    ns_uri = root.tag.split("}")[0].strip("{")
    ns = {"a": ns_uri}
    target = str(numero).strip().lower()
    for art in root.findall(".//a:article", ns):
        eid = (art.get("eId") or "").lower()
        # eId tipico: "art_2"; accetta anche match sul <num>
        num_el = art.find("a:num", ns)
        num_txt = (num_el.text or "").strip() if num_el is not None else ""
        num_norm = re.sub(r"[^0-9a-z]", "", num_txt.lower())
        if eid == f"art_{target}" or eid.endswith(f"_{target}") or num_norm == f"art{target}" or num_norm == target:
            testo = " ".join(t.strip() for t in art.itertext() if t.strip())
            testo = re.sub(r"\s+", " ", testo).strip()
            return num_txt or f"Art. {numero}", testo
    return None


def estrai_tutti(xml_text):
    """Restituisce una lista di (rubrica, testo) per ogni articolo dell'atto."""
    root = ET.fromstring(xml_text.encode("utf-8"))
    ns_uri = root.tag.split("}")[0].strip("{")
    ns = {"a": ns_uri}
    articoli = []
    for art in root.findall(".//a:article", ns):
        num_el = art.find("a:num", ns)
        num_txt = (num_el.text or "").strip() if num_el is not None else ""
        testo = " ".join(t.strip() for t in art.itertext() if t.strip())
        testo = re.sub(r"\s+", " ", testo).strip()
        articoli.append((num_txt or "Art.", testo))
    return articoli


def estrai_indice(xml_text):
    """Restituisce una lista di (num, rubrica) per ogni articolo: solo titoli.

    Economico in token: NON include il corpo degli articoli.
    """
    root = ET.fromstring(xml_text.encode("utf-8"))
    ns_uri = root.tag.split("}")[0].strip("{")
    ns = {"a": ns_uri}
    indice = []
    for art in root.findall(".//a:article", ns):
        num_el = art.find("a:num", ns)
        num_txt = (num_el.text or "").strip() if num_el is not None else ""
        head_el = art.find("a:heading", ns)
        rubrica = ""
        if head_el is not None:
            rubrica = " ".join(t.strip() for t in head_el.itertext() if t.strip())
            rubrica = re.sub(r"\s+", " ", rubrica).strip()
        # Fallback: <heading> vuoto -> rubrica nel primo <paragraph> privo di <num>
        if not rubrica:
            for para in art.findall("a:paragraph", ns):
                if para.find("a:num", ns) is None:
                    rubrica = " ".join(t.strip() for t in para.itertext() if t.strip())
                    rubrica = re.sub(r"\s+", " ", rubrica).strip()
                    break
        indice.append((num_txt or "Art.", rubrica))
    return indice


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--urn", help="URN NIR dell'atto")
    p.add_argument("--data", help="data pubblicazione GU (YYYY-MM-DD)")
    p.add_argument("--codice", help="codice redazionale (es. 24G00121)")
    p.add_argument("--art", help="numero articolo da estrarre (se omesso: tutti gli articoli)")
    p.add_argument("--indice", action="store_true", help="elenca solo numeri e rubriche degli articoli (economico)")
    args = p.parse_args()

    session = requests.Session()
    session.headers.update(UA)

    if args.urn:
        data_pub, codice = risolvi_urn(session, args.urn)
    elif args.data and args.codice:
        data_pub, codice = args.data, args.codice
    else:
        sys.exit("ERRORE: fornire --urn oppure --data e --codice.")

    xml_text = scarica_akn(session, data_pub, codice)

    fonte = f"FONTE: atto codice redazionale {codice} (GU {data_pub}) — fonte Normattiva.it"
    url = (
        f"URL: {BASE}/uri-res/N2Ls?{args.urn}"
        if args.urn
        else f"URL: {BASE}/atto/caricaDettaglioAtto?atto.dataPubblicazioneGazzetta={data_pub}&atto.codiceRedazionale={codice}"
    )

    if args.art:
        # Estrazione di un solo articolo
        ris = estrai_articolo(xml_text, args.art)
        if not ris:
            sys.exit(f"ERRORE: articolo {args.art} non trovato nell'atto {codice}.")
        rubrica, testo = ris
        print(fonte)
        print(url)
        print()
        print(testo)
    elif args.indice:
        # Solo indice: numeri e rubriche degli articoli (economico in token)
        indice = estrai_indice(xml_text)
        if not indice:
            sys.exit(f"ERRORE: nessun articolo trovato nell'atto {codice}.")
        print(fonte)
        print(url)
        print()
        for num_txt, rubrica in indice:
            print(f"{num_txt} {rubrica}".strip())
    else:
        # Estrazione dell'intero atto (tutti gli articoli)
        articoli = estrai_tutti(xml_text)
        if not articoli:
            sys.exit(f"ERRORE: nessun articolo trovato nell'atto {codice}.")
        print(fonte)
        print(url)
        for rubrica, testo in articoli:
            print()
            print(testo)


if __name__ == "__main__":
    main()
