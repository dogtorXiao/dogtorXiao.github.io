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

<!-- # 放好 photos/国家-城市/ 里的图片后
python3 scripts/build_photos.py -->

## 地点定位

城市坐标来自 GeoNames，同名地点按人口优先选择，并优先匹配「市 / 县 / 区 / 特区」等完整名称。
如果某个地点仍然定位不对，在 `assets/geo/overrides.json` 里钉住坐标：

```json
{
  "美国|华盛顿": [38.8951, -77.0364]
}
```

改完运行一次检查脚本，逐条核对：

```
python3 scripts/check_places.py
```

它会列出 `travel.txt` 每个地点解析到的经纬度和匹配到的名称（`override` 表示用了上面的手动坐标）。
