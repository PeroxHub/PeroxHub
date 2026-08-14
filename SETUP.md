# Setup del profilo GitHub animato di perox

## 1. Crea la repo speciale
Se non esiste già, crea una repo pubblica con lo **stesso nome del tuo username**:
`perox/perox`

## 2. Carica i file
Copia in quella repo, mantenendo esattamente questi percorsi:

```
README.md
scripts/generate_terminal.py
.github/workflows/terminal-gif.yml
.github/workflows/snake.yml
```

## 3. Attiva le Actions
Vai su **Settings → Actions → General** della repo e assicurati che:
- "Allow all actions and reusable workflows" sia attivo
- In "Workflow permissions" sia selezionato **Read and write permissions**
  (serve sia allo snake che alla generazione della GIF per fare commit automatici)

## 4. Lancia i workflow la prima volta
Vai su **Actions**, apri "Genera terminal GIF" → **Run workflow**.
Fai lo stesso per "Genera snake animato".
Dopo circa 1-2 minuti:
- `assets/terminal.gif` comparirà nella repo (boot + neofetch retro)
- lo snake verrà pubblicato su un branch `output`

## 5. Verifica i link
Nel README ho usato `perox` come username GitHub. Se non è esatto,
cerca "perox" nel file e sostituiscilo con il tuo username reale in:
- il link della GIF (`raw.githubusercontent.com/perox/perox/...`)
- il link dello snake (`raw.githubusercontent.com/perox/perox/output/...`)

## 6. Fatto
Da quel momento in poi tutto si aggiorna da solo:
- la GIF del terminale ogni lunedì
- lo snake ogni giorno

## Personalizzare la GIF del terminale
Apri `scripts/generate_terminal.py`:
- `BOOT_LINES` → i messaggi di avvio
- `LOGO` → l'ASCII art (puoi generarne una nuova su https://patorjk.com/software/taag/)
- `NEOFETCH` → le righe info stile neofetch (etichetta, valore)

Puoi anche cambiare tema colore passando `color_scheme` a `gifos.Terminal(...)`:
disponibili `yoru` (default), `gruvbox-dark`, `gruvbox-light`, `rose-pine`,
`dracula`, `nord`, `catppuccin-mocha`, `catppuccin-latte`, `onedark`,
`monokai`, `everblush`.
