# Writing an AI-Native Dissertation (AIME-Con 2026 training session)

Materials for the 4-hour, hands-on training session: the slides, the attendee handout, copy-paste prompts, the facilitator run-sheet, and the post-session follow-up. It's one Quarto website.

| File | What |
|---|---|
| `slides.qmd` | The deck (revealjs). Speaker notes on every slide: press `S`. |
| `handout.qmd` | The attendee handout: HTML and PDF (Typst). |
| `prompts/` | The prompts. Text lives in `prompts/_*.md` partials, shared by the prompt pages and the handout. |
| `runsheet.qmd` | Minute-by-minute facilitation, fallbacks, and the day-before checklist. |
| `follow-up.qmd` | Email text for after the session. |
| `index.qmd` | The landing page. |
| `assets/` | The dataimago house styling (Noto Sans; stone/forest/copper). |

## Preview and render

```bash
quarto preview slides.qmd     # the deck, live-reloading
quarto preview                # the whole site
quarto render                 # everything to _site/ (incl. handout.pdf)
```

The handout PDF uses Typst (built into Quarto) and the **Noto Sans** font.

## Publish

`.github/workflows/publish.yml` renders on every push to `main` and deploys to GitHub Pages. It does nothing until Pages is enabled: **Settings → Pages → Source: GitHub Actions**.

## Sources

- The v1.0 session proposal (`AIME_2026_Training_Proposal.tex`).
- The NCME 2026 v0.1 deck (`ncme-2026-ai-native-dissertation.qmd`): the "AI is like a…" exercise, the transmission history, the vocabulary.
- dissertation.ai and the generated repositories as they ship on 2026-10-04 (the hub, the `AGENTS.md` harness, `/ingest`, publish).
