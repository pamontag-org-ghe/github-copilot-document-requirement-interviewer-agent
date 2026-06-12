# Specifica dei Requisiti Software

**per &lt;Progetto&gt;**

Versione 1.0 approvata

Redatto da &lt;autore&gt;

&lt;organizzazione&gt;

&lt;data di creazione&gt;

---

## Indice

- [Cronologia delle Revisioni](#cronologia-delle-revisioni)
- [1. Introduzione](#1-introduzione)
  - [1.1 Scopo del Documento](#11-scopo-del-documento)
  - [1.2 Convenzioni del Documento](#12-convenzioni-del-documento)
  - [1.3 Ambito del Progetto](#13-ambito-del-progetto)
  - [1.4 Riferimenti](#14-riferimenti)
- [2. Descrizione Generale](#2-descrizione-generale)
  - [2.1 Prospettiva del Prodotto](#21-prospettiva-del-prodotto)
  - [2.2 Classi di Utenti e Caratteristiche](#22-classi-di-utenti-e-caratteristiche)
  - [2.3 Ambiente Operativo](#23-ambiente-operativo)
  - [2.4 Vincoli di Progettazione e Implementazione](#24-vincoli-di-progettazione-e-implementazione)
  - [2.5 Assunzioni e Dipendenze](#25-assunzioni-e-dipendenze)
- [3. Funzionalità del Sistema](#3-funzionalità-del-sistema)
  - [3.1 &lt;Funzionalità del Sistema 1&gt;](#31-funzionalità-del-sistema-1)
    - [3.1.1 Descrizione](#311-descrizione)
    - [3.1.2 Sequenze Stimolo/Risposta](#312-sequenze-stimolorisposta)
    - [3.1.3 Requisiti Funzionali](#313-requisiti-funzionali)
  - [3.2 &lt;Funzionalità del Sistema 2&gt;](#32-funzionalità-del-sistema-2)
- [4. Requisiti sui Dati](#4-requisiti-sui-dati)
  - [4.1 Modello Logico dei Dati](#41-modello-logico-dei-dati)
  - [4.2 Dizionario dei Dati](#42-dizionario-dei-dati)
  - [4.3 Report](#43-report)
  - [4.4 Acquisizione, Integrità, Conservazione e Cancellazione dei Dati](#44-acquisizione-integrità-conservazione-e-cancellazione-dei-dati)
- [5. Requisiti delle Interfacce Esterne](#5-requisiti-delle-interfacce-esterne)
  - [5.1 Interfacce Utente](#51-interfacce-utente)
  - [5.2 Interfacce Software](#52-interfacce-software)
  - [5.3 Interfacce Hardware](#53-interfacce-hardware)
  - [5.4 Interfacce di Comunicazione](#54-interfacce-di-comunicazione)
- [6. Attributi di Qualità](#6-attributi-di-qualità)
  - [6.1 Usabilità](#61-usabilità)
  - [6.2 Prestazioni](#62-prestazioni)
  - [6.3 Sicurezza (Security)](#63-sicurezza-security)
  - [6.4 Sicurezza Funzionale (Safety)](#64-sicurezza-funzionale-safety)
  - [6.5 &lt;Altri attributi rilevanti&gt;](#65-altri-attributi-rilevanti)
- [7. Requisiti di Internazionalizzazione e Localizzazione](#7-requisiti-di-internazionalizzazione-e-localizzazione)
- [8. Altri Requisiti](#8-altri-requisiti)
- [9. Glossario](#9-glossario)
- [10. Modelli di Analisi](#10-modelli-di-analisi)

---

## Cronologia delle Revisioni

| Nome | Data | Motivo delle Modifiche | Versione |
|------|------|------------------------|----------|
|      |      |                        |          |
|      |      |                        |          |

---

## 1. Introduzione

*&lt;L'introduzione fornisce una panoramica che aiuta il lettore a capire come è organizzata la specifica e come usarla.&gt;*

### 1.1 Scopo del Documento

*&lt;Identifica il prodotto i cui requisiti software sono specificati in questo documento, comprese la revisione o il numero di rilascio. Descrive i diversi tipi di lettore a cui è destinato il documento, ad esempio sviluppatori, project manager, marketing, utenti, tester, autori della documentazione.&gt;*

### 1.2 Convenzioni del Documento

*&lt;Descrive eventuali standard o convenzioni tipografiche utilizzate, incluso il significato di stili di testo, evidenziazioni o notazioni specifici. Se si etichettano manualmente identificatori univoci dei requisiti, specifica qui il formato per chiunque dovrà aggiungerne altri.&gt;*

### 1.3 Ambito del Progetto

*&lt;Fornisce una breve descrizione del software in oggetto e del suo scopo. Mette in relazione il software con gli obiettivi degli utenti o aziendali e con la strategia di business. Se esiste un documento separato di visione e ambito, fa riferimento ad esso anziché duplicarne il contenuto. Una specifica che descrive un rilascio incrementale di un prodotto in evoluzione deve contenere un proprio ambito come sottoinsieme della visione strategica di lungo periodo. Si può fornire un riepilogo di alto livello delle principali funzionalità del rilascio o delle funzioni significative che esegue.&gt;*

### 1.4 Riferimenti

*&lt;Elenca i documenti o le altre risorse a cui questa specifica fa riferimento. Include collegamenti ipertestuali quando disponibili in una posizione permanente. Possono comprendere guide di stile per l'interfaccia utente, contratti, standard, specifiche dei requisiti di sistema, specifiche di interfaccia o specifiche di prodotti correlati. Fornisce informazioni sufficienti per accedere a ciascun riferimento, tra cui titolo, autore, numero di versione, data, fonte / repository / URL. Suddividi opzionalmente in `Compliance` (documenti citati che impongono requisiti) e `Guidance` (documenti informativi).&gt;*

---

## 2. Descrizione Generale

*&lt;Questa sezione presenta una panoramica di alto livello del prodotto, dell'ambiente in cui sarà utilizzato, degli utenti previsti e dei vincoli, assunzioni e dipendenze note.&gt;*

### 2.1 Prospettiva del Prodotto

*&lt;Descrive il contesto e l'origine del prodotto. È il prossimo membro di una linea di prodotti in crescita, la prossima versione di un sistema maturo, la sostituzione di un'applicazione esistente o un prodotto completamente nuovo? Se questa specifica definisce un componente di un sistema più ampio, indica come questo software si relaziona con il sistema complessivo e identifica le interfacce principali tra i due. Considera l'inclusione di modelli visivi come un diagramma di contesto o una mappa dell'ecosistema per mostrare la relazione del prodotto con gli altri sistemi.&gt;*

### 2.2 Classi di Utenti e Caratteristiche

*&lt;Identifica le diverse classi di utenti che useranno il prodotto e ne descrive le caratteristiche rilevanti. Alcuni requisiti possono valere solo per certe classi di utenti. Identifica le classi favorite. Le classi di utenti sono un sottoinsieme degli stakeholder descritti nel documento di visione e ambito. Le descrizioni sono una risorsa riusabile: se disponibile un catalogo centrale, vi si può fare riferimento invece di duplicare le informazioni.&gt;*

### 2.3 Ambiente Operativo

*&lt;Descrive l'ambiente in cui il software opererà, inclusi piattaforma hardware, sistemi operativi e versioni, ubicazione geografica di utenti, server e database, organizzazioni che ospitano i database / server / siti correlati. Elenca eventuali altri componenti software o applicazioni con cui il sistema deve coesistere. Se è necessario un consistente lavoro di infrastruttura tecnica in parallelo allo sviluppo, considera la creazione di una specifica separata dei requisiti infrastrutturali.&gt;*

### 2.4 Vincoli di Progettazione e Implementazione

*&lt;Descrive eventuali fattori che limitano le opzioni a disposizione degli sviluppatori. Possono comprendere: politiche aziendali o normative; limiti hardware (temporizzazione o memoria); interfacce verso altre applicazioni; tecnologie, strumenti e database obbligatori; requisiti o restrizioni sul linguaggio di programmazione.&gt;*

### 2.5 Assunzioni e Dipendenze

*&lt;Elenca i fattori assunti (a differenza dei fatti noti) che potrebbero influenzare i requisiti dichiarati nella specifica. Possono includere componenti commerciali o di terze parti che si prevede di utilizzare, aspettative di riuso, vincoli sull'ambiente di sviluppo o operativo. Il progetto potrebbe essere impattato se queste assunzioni risultano errate, non condivise o cambiano. Identifica anche le dipendenze del progetto da fattori esterni fuori controllo.&gt;*

---

## 3. Funzionalità del Sistema

*&lt;Questo template illustra l'organizzazione dei requisiti funzionali per **funzionalità del sistema**, i principali servizi forniti dal prodotto. È possibile preferire un'organizzazione per use case, modalità operativa, classe di utenti, classe di oggetti, gerarchia funzionale, stimolo, risposta o combinazioni di questi — qualunque cosa abbia più senso logico per il prodotto in oggetto.&gt;*

### 3.1 &lt;Funzionalità del Sistema 1&gt;

*&lt;Non scrivere letteralmente "Funzionalità del Sistema 1". Indica il nome della funzionalità in poche parole.&gt;*

#### 3.1.1 Descrizione

*&lt;Fornisce una breve descrizione della funzionalità e indica se è di priorità Alta, Media o Bassa.&gt;*

#### 3.1.2 Sequenze Stimolo/Risposta

*&lt;Elenca le sequenze di azioni dell'utente e risposte del sistema che attivano il comportamento definito per questa funzionalità. Corrispondono agli elementi di dialogo associati agli use case.&gt;*

#### 3.1.3 Requisiti Funzionali

*&lt;Elenca per voci i requisiti funzionali specifici associati a questa funzionalità. Sono le capacità software che devono essere implementate affinché l'utente possa svolgere i servizi della funzionalità o completare uno use case. Descrive come il prodotto deve rispondere alle condizioni di errore previste. Usa "TBD" come segnaposto quando l'informazione necessaria non è ancora disponibile. **Per ogni requisito usa il verbo "deve" per le prescrizioni vincolanti, "dovrebbe" per le preferenze, "può" per le concessioni, "sarà / è" per affermazioni di contesto non vincolanti. Evita "dovrà", "deve essere in grado di", "non deve" e la forma passiva.**&gt;*

### 3.2 &lt;Funzionalità del Sistema 2&gt;

*&lt;Ripeti la struttura 3.x.1 / 3.x.2 / 3.x.3 per ciascuna funzionalità aggiuntiva.&gt;*

---

## 4. Requisiti sui Dati

*&lt;Questa sezione descrive vari aspetti dei dati che il sistema consumerà come input, elaborerà o produrrà come output.&gt;*

### 4.1 Modello Logico dei Dati

*&lt;Un modello dei dati è una rappresentazione visiva degli oggetti dati e delle collezioni che il sistema elaborerà, con le relazioni tra di essi. Includi un modello dei dati per le operazioni di business affrontate dal sistema, o una rappresentazione logica per i dati che il sistema stesso manipolerà. I modelli dei dati sono comunemente realizzati come diagrammi entità-relazione.&gt;*

### 4.2 Dizionario dei Dati

*&lt;Il dizionario dei dati definisce la composizione delle strutture dati e il significato, tipo, lunghezza, formato e valori ammessi per gli elementi che le compongono. In molti casi è preferibile conservare il dizionario dei dati come artefatto separato anziché embedderlo nella specifica, aumentandone così il potenziale di riuso in altri progetti.&gt;*

### 4.3 Report

*&lt;Se l'applicazione genererà report, identificali qui e descrivine le caratteristiche. Se un report deve seguire un layout predefinito, lo si può specificare qui come vincolo, eventualmente con un esempio. Altrimenti, concentrati sulla descrizione logica del contenuto, dell'ordinamento, dei livelli di totalizzazione, rimandando il layout dettagliato alla fase di progettazione.&gt;*

### 4.4 Acquisizione, Integrità, Conservazione e Cancellazione dei Dati

*&lt;Se rilevante, descrivi come i dati vengono acquisiti e mantenuti. Indica i requisiti per proteggere l'integrità dei dati del sistema. Identifica eventuali tecniche specifiche necessarie, come backup, checkpoint, mirroring o verifica dell'accuratezza dei dati. Definisce le politiche di conservazione e cancellazione, inclusi dati temporanei, metadati, dati residui (come record cancellati), dati in cache, copie locali, archivi e backup intermedi.&gt;*

---

## 5. Requisiti delle Interfacce Esterne

*&lt;Questa sezione fornisce informazioni per garantire che il sistema comunichi correttamente con gli utenti e con gli elementi hardware o software esterni.&gt;*

### 5.1 Interfacce Utente

*&lt;Descrive le caratteristiche logiche di ciascuna interfaccia tra il prodotto software e gli utenti. Può includere immagini di esempio delle schermate, standard GUI o guide di stile per la famiglia di prodotti da rispettare, vincoli di layout, pulsanti e funzioni standard (es. aiuto) che appaiono in ogni schermata, scorciatoie da tastiera, standard di visualizzazione dei messaggi di errore, ecc. Definisce i componenti software per cui è necessaria un'interfaccia utente. I dettagli di progettazione dell'interfaccia utente vanno documentati in una specifica separata.&gt;*

### 5.2 Interfacce Software

*&lt;Descrive le connessioni tra questo prodotto e altri componenti software (identificati per nome e versione), inclusi altre applicazioni, database, sistemi operativi, strumenti, librerie, siti web e componenti commerciali integrati. Indica scopo, formati e contenuti di messaggi, dati e valori di controllo scambiati tra i componenti software. Specifica i mapping di input e output tra i sistemi e le traduzioni necessarie affinché i dati passino da un sistema all'altro. Descrive i servizi richiesti da o verso componenti software esterni e la natura delle comunicazioni inter-componente. Identifica i dati che saranno scambiati o condivisi tra componenti software. Specifica i requisiti non funzionali che influenzano l'interfaccia, come livelli di servizio per tempi di risposta e frequenza, o controlli e restrizioni di sicurezza.&gt;*

### 5.3 Interfacce Hardware

*&lt;Descrive le caratteristiche di ciascuna interfaccia tra i componenti software e hardware (se presenti) del sistema. Questa descrizione può includere i tipi di dispositivo supportati, le interazioni dati e di controllo tra software e hardware, e i protocolli di comunicazione utilizzati. Elenca gli input e gli output, i loro formati, valori validi o range, ed eventuali problemi di temporizzazione di cui gli sviluppatori devono essere consapevoli. Se queste informazioni sono estese, considera un documento separato per la specifica delle interfacce.&gt;*

### 5.4 Interfacce di Comunicazione

*&lt;Definisce i requisiti per qualunque funzione di comunicazione che il prodotto utilizzerà, inclusi e-mail, browser web, protocolli di rete e moduli elettronici. Specifica la formattazione dei messaggi pertinente. Indica le questioni di sicurezza o cifratura, le velocità di trasferimento dati, l'handshaking e i meccanismi di sincronizzazione. Indica eventuali vincoli su queste interfacce, come l'accettazione o meno degli allegati e-mail.&gt;*

---

## 6. Attributi di Qualità

### 6.1 Usabilità

*&lt;Specifica i requisiti relativi alle caratteristiche che renderanno il software "facile da usare". L'usabilità comprende: facilità d'uso, facilità di apprendimento, memorabilità, prevenzione/gestione/recupero degli errori, efficienza delle interazioni, accessibilità ed ergonomia. A volte questi requisiti possono entrare in conflitto tra loro (ad esempio facilità d'uso vs facilità di apprendimento). Indica gli standard o le linee guida di design dell'interfaccia utente a cui l'applicazione deve conformarsi.&gt;*

### 6.2 Prestazioni

*&lt;Indica i requisiti di prestazione specifici per le varie operazioni del sistema. Se i requisiti prestazionali sono diversi per i diversi requisiti funzionali o funzionalità, è opportuno specificarli accanto al rispettivo requisito funzionale anziché raggrupparli in questa sezione.&gt;*

### 6.3 Sicurezza (Security)

*&lt;Specifica i requisiti relativi a questioni di sicurezza o privacy che limitano l'accesso o l'uso del prodotto. Possono riferirsi a sicurezza fisica, sui dati o software. I requisiti di sicurezza spesso derivano da regole di business: identifica le politiche o normative di sicurezza/privacy a cui il prodotto deve conformarsi. Se documentate in un repository di regole di business, fai semplicemente riferimento ad esse.&gt;*

### 6.4 Sicurezza Funzionale (Safety)

*&lt;Specifica i requisiti relativi a possibili perdite, danni o lesioni che potrebbero derivare dall'uso del prodotto. Definisce eventuali misure di sicurezza o azioni da intraprendere, nonché azioni potenzialmente pericolose che devono essere prevenute. Identifica eventuali certificazioni, politiche o normative di safety a cui il prodotto deve conformarsi.&gt;*

### 6.5 &lt;Altri attributi rilevanti&gt;

*&lt;Crea una sezione separata nella specifica per ciascun ulteriore attributo qualitativo del prodotto, per descrivere caratteristiche importanti per clienti o sviluppatori. Possibilità: disponibilità, efficienza, installabilità, integrità, interoperabilità, modificabilità, portabilità, affidabilità, riusabilità, robustezza, scalabilità e verificabilità. Scrivi questi requisiti in modo specifico, quantitativo e verificabile. Chiarisci le priorità relative tra gli attributi (es. sicurezza > prestazioni).&gt;*

---

## 7. Requisiti di Internazionalizzazione e Localizzazione

*&lt;I requisiti di i18n / l10n garantiscono che il prodotto sia adatto all'uso in nazioni, culture e località geografiche diverse da quella di creazione. Tali requisiti possono affrontare differenze in: valuta; formati di date, numeri, indirizzi e numeri di telefono; lingua, inclusi convenzioni nazionali per la stessa lingua (es. inglese britannico vs americano), simboli usati, set di caratteri; ordine nome / cognome; fusi orari; normative e leggi internazionali; questioni culturali e politiche; formati cartacei in uso; pesi e misure; voltaggi elettrici e forme di presa; e molti altri.&gt;*

---

## 8. Altri Requisiti

*&lt;Esempi: requisiti legali, normativi o finanziari di compliance, e requisiti di conformità a standard; requisiti per installazione, configurazione, avvio e arresto del prodotto; requisiti di logging, monitoraggio e audit trail. Anziché raggruppare tutti questi sotto "Altri", aggiungi nuove sezioni al template pertinenti al progetto. Ometti questa sezione se tutti i requisiti sono già coperti dalle altre sezioni.&gt;*

---

## 9. Glossario

*&lt;Definisce eventuali termini specialistici che il lettore deve conoscere per comprendere la specifica, inclusi acronimi e abbreviazioni. Sviluppa per esteso ciascun acronimo e fornisce la definizione. Considera la costruzione di un glossario aziendale riusabile su più progetti e l'inclusione per riferimento dei termini che riguardano questo progetto.&gt;*

| Termine | Definizione |
|---------|-------------|
|         |             |

---

## 10. Modelli di Analisi

*&lt;Questa sezione opzionale include o rimanda a modelli di analisi rilevanti come diagrammi data flow, alberi di funzionalità, diagrammi a stati o entità-relazione. Si può preferire inserire alcuni modelli nelle sezioni pertinenti della specifica anziché raccoglierli tutti alla fine.&gt;*
