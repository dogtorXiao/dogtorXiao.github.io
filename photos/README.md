# photos/

每个地方一个文件夹，命名方式：`国家-城市`，例如：

- `photos/加拿大-蒙特利尔/`
- `photos/奥地利-维也纳/`

图片支持 jpg / jpeg / png / webp / gif / avif，每个地点最多显示 4 张。

**加了或删了照片后，运行一次：**

```
python3 scripts/build_photos.py
```

它会重写根目录的 `photos.json`（地图页读取的清单），然后提交这个文件即可。
如果不重新生成，地图只会尝试该文件夹里的 `cover.jpg`。

文件夹名要和 `travel.txt` 里的「国家-城市」完全一致；
想只显示指定几张，可在 `travel.txt` 第五段写文件名（逗号分隔）。
