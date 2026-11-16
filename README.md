# Zixuan Xiao — Profile Homepage

Source for **https://dogtorxiao.github.io**

A static site: no build step, no external fonts, no tracking scripts.
Bilingual (中 / EN) via the switch in the top-right corner.

- `index.html` — the homepage
- `map.html` — travel map, reads `travel.txt`
- `travel.txt` — one line per place: `date | country | city | note | photos(optional)`
- `photos/<country>-<city>/` — photos for each place, listed automatically
- `assets/leaflet/` — vendored Leaflet 1.9.4
- `Portrait.jpg`, `Resume.pdf` — profile photo and CV

Map tiles © OpenStreetMap contributors. City coordinates are geocoded via Nominatim
and cached in the browser.
