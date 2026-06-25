# law_articles/

Verbatim cache of Italian-law text fetched by the `Requirements Interviewer` agent through the
`law-expert` subagent (which reads the official text from [Normattiva.it](https://www.normattiva.it/)
via the `normattiva-crawler` skill).

- Each `.txt` file holds the **literal** text returned by `law-expert`, including its `Fonte: …`
  citation line. The text is never summarised, paraphrased, translated or interpreted.
- The agent checks this folder **before** invoking `law-expert`: if a matching file already exists,
  it reuses the cached text instead of calling the subagent again (even in a new conversation).

## File naming

- Single article: `<tipo-atto>-<numero>-<anno>-art-<n>.txt` — e.g. `legge-300-1970-art-18.txt`.
- Full act: `<tipo-atto>-<numero>-<anno>-completo.txt` — e.g. `decreto-legislativo-103-2024-completo.txt`.
