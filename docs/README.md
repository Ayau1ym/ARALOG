# ARALOG

ARALOG is an offline-first static atlas for testing one engineering analogy: how dust adheres to, shades and can be cleaned off solar hardware. Its claim is **Analog fitness depends on the question being asked.** It frames Aralkum as a screening site for one Mars dust question, not as Mars or a lunar analog.

## Run

Serve the project root with a static server, for example `python -m http.server 8000`, then visit `/site/`. The browser loads only local HTML, CSS, JavaScript and JSON. NASA POWER data is included as a snapshot. No CDN, map tile or font dependency is required. Earth and Mars locators are explicitly schematic; no NASA imagery is bundled.

## Data update

Run `python data/fetch/fetch_power.py` online to refresh the NASA POWER 2025 snapshot. Run `python data/fetch/fetch_gibs.py` only when intentionally bundling imagery; verify scene meaning and attribution first. The EMIT helper describes a manual coverage-inspection gate.

## Public release checklist

1. Confirm 2026 rules, Project tab deadline/status, team registration and official challenge selection.
2. Confirm publication consent/credits for paper, images and names.
3. Review `SHOW_AUTHOR_NAME=false`; retain generic student credit unless author and teacher agree otherwise. No face photos or author voice/video.
4. Inspect EMIT coverage before adding mineral observations.
5. Add public repo URL and Zenodo DOI after publication; do not invent either.
6. Include references and NASA attribution; state project is independent and not NASA-affiliated.

## Contents

`site/` product; `data/fetch/` scripts; `data/processed/` snapshots; `docs/` science/methods/change log/AI disclosure; `pitch/` deck and narrative; `submission/` copy and references.
