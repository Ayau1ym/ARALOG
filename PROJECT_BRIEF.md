# Project brief

## What exists

The supplied research paper and presentation describe three field samples and three experiments. The strongest concrete observation is a miniature PV output-voltage change from 0.30 V (clean) to 0.22 V with friction-charged Aralkum dust under the paper's stated bench setup. Other usable results are aqueous-extract Fe/Cu/Mn, a qualitative electrical comparison, and a prototype cleaning result reported in the paper. A compact demo ZIP includes specimen photos, a lab CSV, source notes, claim caveats, and a prototype static web app.

The larger ARALOG ZIP is essentially the demo plus a scorecard. The prototype's content is reusable, but its visual design and runtime reliance on CDN-hosted fonts/maps should not be retained. It lacks a preprocessed NASA dataset and an Earth-to-Earth analog comparison. The old source notes already warn against treating extract Fe as bulk Fe or voltage as power.

## Reusable

- Study methods, sample coordinates and reported values, with qualifications from the supplied instructions.
- A specimen set photograph from the supplied ZIP is included; it shows labeled samples only, no person.
- The question-led, task-specific analog framing.
- NASA POWER snapshots for the three sample locations, fetched and included in `data/processed/`.
- NASA InSight power endpoints and Opportunity cleaning context as published references.

## Weak or corrected

- The paper and slides sometimes overstate “hypothesis confirmed,” analog equivalence and the role of iron. Aqueous-extract metals are not bulk mineralogy and do not demonstrate a Mars match.
- The cited Xi et al. 2025 paper covers satellite aerosol retrievals during an Aralkum saline dust storm; it does not establish the proposed carbonate/sulfate versus iron-oxide/clay comparison. That headline claim is excluded.
- 25.6% cleaning is reported in the paper but lacks run count, raw masses and polarity; displayed as preliminary single-prototype report.
- The voltage loss is a voltage measurement, not power/efficiency, and does not separate optical shading from electrostatics.
- The older implementation uses CDN Leaflet/fonts and live map dependencies. The rebuild uses local HTML/CSS/JS and local NASA POWER snapshots. Its point plot is schematic, with no streamed tile layer.
- EMIT sample-coordinate coverage, March 2020 GIBS event identification, MERRA-2/MODIS dust optical depth, Mars MOLA context, and the 2026 submission guide remain unverified or unbundled. No data are fabricated to fill these gaps.

## Privacy and identity

Default public display is `student researcher, NIS Kyzylorda`; the public build has `SHOW_AUTHOR_NAME=false`, no face photo and no author video link. The author and teacher must review that choice before publication. No NASA or other agency logos are used. The site states that it is independent and not NASA-affiliated.

## Scope shipped

Tier 1 core: hook, sample atlas, separate Mars context, question-specific analogy matrix, three experiment notebook sections, evidence ledger, provenance, limits, source register, methods, credits, AI disclosure, submission copy, 7-slide pitch and notes. Tier 2/Tier 3 extras were deferred to preserve a verifiable core.
