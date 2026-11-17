#!/usr/bin/env python3
"""Rebuild photos.json from the photos/ folder.

Usage:  python3 scripts/build_photos.py
"""
import json
import os
import re

BASE = 'photos'
OUT = 'photos.json'
IMAGE_EXT = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.avif')


def sort_key(name):
    return [int(part) if part.isdigit() else part.lower()
            for part in re.split(r'(\d+)', name)]


def main():
    manifest = {}
    for folder in sorted(os.listdir(BASE)):
        path = os.path.join(BASE, folder)
        if not os.path.isdir(path):
            continue
        files = [f for f in os.listdir(path) if f.lower().endswith(IMAGE_EXT)]
        if not files:
            continue
        files.sort(key=sort_key)
        manifest[folder] = ['photos/%s/%s' % (folder, f) for f in files]
    with open(OUT, 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, ensure_ascii=False, separators=(',', ':'))
    print('%d folders, %d photos' % (len(manifest), sum(len(v) for v in manifest.values())))


if __name__ == '__main__':
    main()
