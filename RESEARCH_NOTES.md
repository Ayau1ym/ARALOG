# Research notes

Retrieved 2026-11-15. URLs were opened or queried on this date. Lack of coverage inspection is not a negative finding.

## Challenge and submission

- Official challenge: https://www.spaceappschallenge.org/2026/challenges/permanent-moon-base-locations-and-mars/ — asks teams to use open Earth, Moon and Mars data to identify and characterize terrestrial analogs and present a map, visualization or tool. Mars-only is consistent with the wording but verify challenge-specific judging page.
- 2026 event page: https://www.spaceappschallenge.org/2026/ — submission window displayed as Nov 14 09:00 to Nov 15 23:59 local time. Author must verify current deadline and submitted state on her Project tab.
- Official current Project Submission Guide: UNVERIFIED; no accessible 2026 guide was located in this pass. A 2020 guide (not a substitute for current rules) says resource integration must be shown and demo is <=7 slides OR <=30-second video: https://2020.spaceappschallenge.org/assets/documents/460/Space_Apps_2020_Project_Submission_Guide.pdf. Confirm current rules before final upload.
- Official 2026 judging guide and axis names/weights: UNVERIFIED. The five axes in this project brief are user-supplied; do not claim independent verification.

## NASA data and mission sources

- NASA POWER daily/monthly point service docs: https://power.larc.nasa.gov/docs/services/api/temporal/daily/ — parameter and API availability verified. Three 2025 monthly point snapshots for N1/N2/N3 were retrieved from the API on 2026-11-15 and saved to `data/processed/nasa_power_monthly_2025.json`; exact request URLs and values are embedded there. Environmental context only, not mineral/soiling data. Docs: https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/.
- NASA GIBS API docs: https://nasa-gibs.github.io/gibs-api-docs/ — service found; no image bundled. MODIS/Aqua scene on 2020-03-24 and identification as an Aralkum saline dust storm: UNVERIFIED. The supplied demo used 2026-07-28; its map snapshot was not reused.
- EMITL2BMIN product: https://data.nasa.gov/dataset/emit-l2b-estimated-mineral-identification-and-band-depth-and-uncertainty-60-m-v001-7fe29 and DOI https://doi.org/10.5067/EMIT/EMITL2BMIN.001. Product exists; no inspected granule or valid pixel at sample coordinates, so no site-mineral claims.
- MERRA-2/MODIS dust optical depth for this region: UNVERIFIED; no snapshot or claim included.
- Mars Trek/MOLA service references: https://trek.nasa.gov/mars/ and https://trek.nasa.gov/tiles/apidoc/trekAPI.html?body=mars — source/service found, but no elevation tile shipped. TES dust-cover data source/product record: UNVERIFIED.
- Mars MOLA/TES context and exact source record: not included in offline map. Mars context linked to NASA facts: https://science.nasa.gov/mars/facts/.
- NASA/JPL InSight landing-site reference: https://www.jpl.nasa.gov/news/press_kits/insight/launch/mission/landing-site/ — western Elysium Planitia, centered at about 4.5° N, 135.9° E. Used only for a schematic locator.
- InSight power resource: https://science.nasa.gov/resource/insights-power-generation-after-landing-and-spring-2022/ reports ~5,000 Wh/sol after landing and ~500 Wh/sol by spring 2022; dust accumulation is implicated. Only these two endpoints are shown, with no interpolation.

## Scientific references and verification

- Cannon et al. (2019), MGS-1 open standard, DOI 10.1016/j.icarus.2018.08.019: https://doi.org/10.1016/j.icarus.2018.08.019. DOI resolves; article/source identity verified. MGS-1 is a simulant, not tested by this student. Median size 70.51 μm and FeO 10.60 wt% are cited as published specifications; FeO is not comparable with aqueous-extract Fe.
- Space Resource Technologies / Exolith Lab product information: https://spaceresourcetech.com/products/mgs-1-mars-global-simulant — cited reference specification; no physical simulant tested.
- Xi et al. (2025), ACP 25, 7403–7429, DOI 10.5194/acp-25-7403-2025: https://doi.org/10.5194/acp-25-7403-2025. DOI resolves; paper is about multisensor aerosol-product consistency for a saline Aralkum dust storm. It does not support the proposed mineralogical contrast; that claim is removed.
- Lorenz et al. (2021), “Lander and rover histories of dust accumulation on and removal from solar arrays on Mars,” DOI 10.1016/j.pss.2021.105337: https://doi.org/10.1016/j.pss.2021.105337. DOI resolves; published dust-factor decrease range 0.05–2% per sol, typical ~0.2% per sol. Not used in a model.
- Arvidson et al. (2011), Opportunity overview, DOI 10.1029/2010JE003746: https://doi.org/10.1029/2010JE003746. DOI resolves; paper lists wind cleaning sols 520, 1150, 1305, 1520 (minor), 1620, 1846 (minor), 1990 (minor), 2300. The 375→620 Wh/sol mid-2014 item was not verified from authoritative NASA source; excluded.
- Chide et al. (2025), Nature 647, 865–869, DOI 10.1038/s41586-025-09736-y: https://doi.org/10.1038/s41586-025-09736-y. DOI resolves; 55 triboelectric discharge events over two Martian years reported from Perseverance observations. This does not prove Aralkum behaves like Mars.
- Kazakhstan MPC Order 157-p (21 May 2007): primary text and exact analyte applicability UNVERIFIED; no compliance claim is shown.
- LHS-1 lunar simulant and Moon note: deferred; no Moon claim in Tier 1.

## Interpretation guardrails

Evidence labels (MEASURED ours, PUBLISHED, HYPOTHESIS, NOT TESTED) use icon and text. There is no global similarity percentage. “Iron in aqueous extract” remains mg/dm³; MGS-1 FeO remains wt%. Study limits shown in the UI: n=3; chemistry covers only Fe/Cu/Mn; particle size not measured; tests run in Earth air, not CO₂ / low pressure / UV.
