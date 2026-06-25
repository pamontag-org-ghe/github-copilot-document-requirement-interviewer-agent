---
name: normattiva-crawler
description: Recupera il testo ufficiale di leggi, decreti e articoli dalla banca dati Normattiva.it (https://www.normattiva.it/). Use when l'utente chiede il testo di una norma, un articolo, un decreto legislativo o una legge italiana.
---

# Normattiva Crawler

Recupera il testo letterale delle norme italiane da [Normattiva](https://www.normattiva.it/). Funziona come un RAG: scarica l'atto, estrae il testo richiesto, lo cita. **Non interpretare, non commentare, non usare conoscenza pregressa.**

## Metodo: script Python

Usare [scripts/estrai_articolo.py](scripts/estrai_articolo.py). Lo script scarica l'atto **localmente** (export Akoma Ntoso XML) e stampa a video il testo letterale. **Non serve leggere il codice dello script: tutti i parametri sono documentati qui sotto.**

Identificare l'atto con **una** di queste due forme:
- `--urn "<URN NIR>"` — se si conosce l'URN dell'atto;
- `--data <YYYY-MM-DD> --codice <codice redazionale>` — se si conoscono data GU e codice.

Il parametro `--art` decide **quanto** testo estrarre:

### Un solo articolo — con `--art`
Usare quando l'utente chiede un articolo preciso (risparmio di token: l'atto intero non entra nel contesto).
```
python scripts/estrai_articolo.py --urn "urn:nir:stato:decreto.legislativo:2024-07-12;103" --art 2
python scripts/estrai_articolo.py --data 2024-07-18 --codice 24G00121 --art 2
```

### Atto completo (tutti gli articoli) — senza `--art`
Usare quando l'utente vuole il **testo integrale**: lo script estrae e mostra **tutti** gli articoli dell'atto. **Costo elevato in token.**
```
python scripts/estrai_articolo.py --urn "urn:nir:stato:legge:2025-12-02;181"
python scripts/estrai_articolo.py --data 2025-12-04 --codice 25G00200
```

### Indice degli articoli — `--indice`
Usare quando l'utente vuole solo l'elenco: lo script stampa **numero + rubrica** di ogni articolo, **senza** il corpo. Economico in token.
```
python scripts/estrai_articolo.py --urn "urn:nir:stato:legge:2025-12-02;181" --indice
```

Restituire all'utente il testo prodotto, senza modifiche.

## Come costruire l'URN

Schema URN NIR:
```
urn:nir:stato:<tipo.atto>:<AAAA-MM-GG>;<numero>
```
Esempi:
- `urn:nir:stato:decreto.legislativo:2024-07-12;103`
- `urn:nir:stato:legge:1970-05-20;300`
- `urn:nir:stato:decreto.del.presidente.della.repubblica:2000-12-28;445`

Se l'atto esatto non è noto, cercarlo prima su `https://www.normattiva.it/` (ricerca per parole chiave) per ricavare data GU e codice redazionale, oppure l'URN.

## Requisiti

Lo script richiede `requests`. Se manca: `pip install requests`.

## Regole

- Se l'utente indica un articolo, estrarre **solo** quell'articolo (`--art`).
- Se l'utente **non** indica l'articolo, **chiedere prima** se vuole l'**indice** (`--indice`, economico) oppure il **testo integrale** (senza `--art`, **avvisando del costo elevato in token**). Scaricare il testo solo dopo la scelta.
- Restituire il testo **letterale** prodotto dallo script, **verbatim e integrale**.
- **VIETATO riassumere o tabulare il testo degli articoli.** Non sostituire il corpo degli articoli con descrizioni inventate: è un'interpretazione, non la norma. L'unica tabella ammessa è l'indice (numero + rubrica ufficiale) di `--indice`.
- Citare sempre la fonte: tipo atto, numero, data, articolo.
- Se l'articolo o l'atto non esistono su Normattiva, dichiararlo. Non inventare.

## Formato risposta

```
Fonte: [tipo atto, numero, data] — Art. [n] (o "testo completo")

[testo letterale]
```
