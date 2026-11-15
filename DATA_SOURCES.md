# Data sources

Snapshot retrieved 2026-11-15. Exact request URLs per site are recorded in `data/processed/nasa_power_monthly_2025.json`.

| Dataset | Instrument/source | Use | Processing | Licence |
|---|---|---|---|---|
| NASA POWER monthly point 2025 | POWER API; surface radiation and meteorological parameters | Local environmental context for N1/N2/N3 | API values copied into JSON; chart uses 12 monthly keys and excludes annual summary | NASA data; cite POWER |
| Study specimen photograph | Student research materials in supplied demo archive | Specimen gallery only | Original sample-set photograph copied without alteration; no person shown | Author/teacher permission to confirm |
| Student lab values | supplied student research paper (2026) | Extract chemistry, electrical response, panel voltage, prototype cleaning | Retained with reported units and caveats | Author-provided; confirm publication permissions |
| InSight power endpoints | NASA/JPL mission graphic, link in RESEARCH_NOTES | Mission context | Two published endpoints only; no interpolation | NASA attribution |
| MGS-1 specifications | Cannon 2019; Space Resource Technologies / Exolith Lab | Published reference, not a tested sample | Literature values retained as published | Follow cited source terms |
| EMITL2BMIN | NASA/LP DAAC | No values included; coverage inspection pending | Not processed | NASA open data; follow product guide |
| GIBS MODIS/Aqua | NASA GIBS | Optional image fetcher; no image shipped | Request helper only | NASA attribution required |

No MERRA-2/MODIS aerosol optical depth, EMIT granule, MOLA tile, or 2020-03-24 image is presented as a processed dataset in this build.
