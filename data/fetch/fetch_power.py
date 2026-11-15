#!/usr/bin/env python3
"""Fetch NASA POWER monthly snapshots for the three ARALOG seed sites."""
import json
import urllib.request
import datetime
import pathlib

OUT = pathlib.Path(__file__).resolve().parents[1] / "processed" / "nasa_power_monthly_2025.json"
SITES = [("N1", 45.398333, 59.795556), ("N2", 45.633333, 60.250021), ("N3", 44.828889, 65.519722)]
rows = []
for name, lat, lon in SITES:
    url = ("https://power.larc.nasa.gov/api/temporal/monthly/point?"
           f"parameters=ALLSKY_SFC_SW_DWN,T2M,RH2M,WS10M&community=RE&longitude={lon}&latitude={lat}&start=2025&end=2025&format=JSON")
    with urllib.request.urlopen(url, timeout=30) as response:
        rows.append({"id": name, "lat": lat, "lon": lon, "request_url": url,
                     "data": json.load(response)["properties"]["parameter"]})
OUT.write_text(json.dumps({"retrieved": datetime.date.today().isoformat(), "year": 2025, "sites": rows}, indent=2), encoding="utf-8")
print(f"Wrote {OUT}")
