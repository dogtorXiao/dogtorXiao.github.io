# Zixuan Xiao — Academic Homepage

Source for **https://dogtorxiao.github.io**

A static site: no build step, no external fonts, no tracking scripts.
Bilingual (中 / EN) via the switch in the top-right corner.

- `index.html` — the homepage
- `map.html` — travel map; reads `travel.txt`
- `travel.txt` — one line per place: `date | country | city | note | photos(optional)`
- `photos/<country>-<city>/` — photos for each place
- `photos.json` — photo index used by the map; rebuild with `python3 scripts/build_photos.py`
- `assets/geo/` — offline map data:
  - `world.json` — country outlines, from Natural Earth (public domain)
  - `countries.json` — country names → ISO codes
  - `cities/<ISO>.json` — city coordinates, derived from GeoNames (CC BY 4.0)
- `assets/leaflet/` — vendored Leaflet 1.9.4
- `Portrait.jpg`, `Resume.pdf`

The map makes **no external requests**: outlines, coordinates, and photo lists are all
served from this repository, so it keeps working on networks where OpenStreetMap tiles
or Nominatim are unavailable. Only the attribution links point outside.
