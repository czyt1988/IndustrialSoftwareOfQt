"""抓取书中收录项目的仓库元数据，用于生成附录 A 的索引表。

用法：
    python tools/fetch_repo_meta.py

结果写入 .cache/repo-meta.json（该目录不入库）。数据仅作为写作与校对参考，
正式发布前应人工核对许可证与项目状态。
"""

from __future__ import annotations

import json
import pathlib
import time
import urllib.error
import urllib.request

REPOS = [
    # 几何 / CAD
    "FreeCAD/FreeCAD",
    "fougue/mayo",
    "mikowiec/rhioCAD",
    "qcad/qcad",
    "LibreCAD/LibreCAD",
    "DLR-SC/tigl",
    "krishauser/Klampt",
    "OpenNURBS/OpenNURBS",
    # EDA
    "KiCad/kicad-source-mirror",
    "LibrePCB/LibrePCB",
    # CAE / FEM
    "OpenFOAM/OpenFOAM-dev",
    "Kitware/ParaView",
    "DISOGitHub/FastCAE",
    # 可视化
    "Kitware/VTK",
    "commontk/CTK",
    "InsightSoftwareConsortium/ITK",
    "Slicer/Slicer",
    "inviwo/inviwo",
    "visit-dav/visit",
    "KDE/labplot",
    "KDAB/KDChart",
    "jkriege2/JKQtPlotter",
    # GIS
    "qgis/QGIS",
    "tumic0/GPXSee",
]

FIELDS = (
    "full_name",
    "html_url",
    "description",
    "language",
    "stargazers_count",
    "pushed_at",
    "archived",
    "default_branch",
    "topics",
)


def fetch(full_name: str) -> dict:
    url = f"https://api.github.com/repos/{full_name}"
    req = urllib.request.Request(url, headers={"User-Agent": "qt-industrial-book"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.load(resp)
    meta = {k: data.get(k) for k in FIELDS}
    lic = data.get("license") or {}
    meta["license"] = lic.get("spdx_id")
    meta["license_name"] = lic.get("name")
    return meta


def main() -> None:
    out = pathlib.Path(".cache")
    out.mkdir(exist_ok=True)
    results: dict[str, dict | str] = {}
    for name in REPOS:
        try:
            results[name] = fetch(name)
            print(f"ok   {name}")
        except urllib.error.HTTPError as exc:
            results[name] = f"HTTP {exc.code}"
            print(f"fail {name}: HTTP {exc.code}")
        except Exception as exc:  # noqa: BLE001 - 记录即可，不中断整批
            results[name] = repr(exc)
            print(f"fail {name}: {exc}")
        time.sleep(0.4)
    (out / "repo-meta.json").write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
