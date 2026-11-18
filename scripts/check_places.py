#!/usr/bin/env python3
"""检查 travel.txt 里每条记录解析到的坐标。

用法：  python3 scripts/check_places.py

如果某条坐标不对，在 assets/geo/overrides.json 里加一行：
    "国家|城市": [纬度, 经度]
它的优先级最高。改完重新运行本脚本确认。
"""
import json
import os

SUFFIXES = ['市', '特区', '特别行政区', '自治州', '地区', '县', '区', '旗', '盟']
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(path, default):
    try:
        with open(os.path.join(ROOT, path), encoding='utf-8') as fh:
            return json.load(fh)
    except Exception:
        return default


def main():
    countries = load('assets/geo/countries.json', {})
    overrides = load('assets/geo/overrides.json', {})
    cache = {}

    def lookup(city, country):
        key = '%s|%s' % (country, city)
        if key in overrides:
            return overrides[key], 'override'
        cc = countries.get(country) or countries.get(country.lower())
        if not cc:
            return None, None
        if cc not in cache:
            cache[cc] = load('assets/geo/cities/%s.json' % cc, {})
        data = cache[cc]
        base = city
        for s in SUFFIXES:
            if len(base) > len(s) and base.endswith(s):
                base = base[:-len(s)]
        keys = [base + s for s in SUFFIXES]
        if base != city:
            keys.append(city)
        keys.append(base)
        for k in keys:
            if k in data:
                return data[k], k
        for k in keys:
            if k.lower() in data:
                return data[k.lower()], k
        return None, None

    rows = []
    with open(os.path.join(ROOT, 'travel.txt'), encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 3:
                rows.append((parts[0], parts[2], parts[1]))

    missing = []
    for date, city, country in rows:
        hit, matched = lookup(city, country)
        if hit:
            print('%-10s %-12s %-8s %8.3f, %9.3f   (%s)' % (date, city, country, hit[0], hit[1], matched))
        else:
            missing.append('%s (%s)' % (city, country))
            print('%-10s %-12s %-8s -- 未定位' % (date, city, country))

    print()
    print('共 %d 条，未定位 %d 条%s' % (
        len(rows), len(missing), ('：' + '、'.join(missing)) if missing else ''))
    if missing:
        print('可以把未定位的城市改成更完整的名字，或在 assets/geo/overrides.json 里钉坐标。')


if __name__ == '__main__':
    main()
