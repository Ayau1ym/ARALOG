#!/usr/bin/env python3
"""Fetch NASA GIBS MODIS/Aqua true-color imagery for offline display."""
import pathlib
import urllib.request

out = pathlib.Path(__file__).resolve().parents[1] / "processed" / "aralkum_modis_aqua_2020-03-24.jpg"
url = ("https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?SERVICE=WMS&REQUEST=GetMap&VERSION=1.1.1&"
       "LAYERS=MODIS_Aqua_CorrectedReflectance_TrueColor&STYLES=&FORMAT=image/jpeg&TRANSPARENT=false&"
       "HEIGHT=720&WIDTH=1100&SRS=EPSG:4326&BBOX=43,56,49,64&TIME=2020-03-24")
with urllib.request.urlopen(url, timeout=30) as response:
    out.write_bytes(response.read())
print(f"Wrote {out}; verify the scene/date and event attribution before describing it as a dust storm.")
