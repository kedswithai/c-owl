#!/usr/bin/env python3
"""
ダウンロードフォルダで最新のファイルを見つけるスクリプト
Find the latest downloaded file in the Downloads folder.
"""

import os
import sys
from pathlib import Path


def find_latest_download(downloads_dir: str | None = None) -> Path | None:
    """
    ダウンロードフォルダ内で最新のファイルを返す。

    Args:
        downloads_dir: ダウンロードフォルダのパス。省略時はデフォルトパスを使用。

    Returns:
        最新ファイルの Path。ファイルが存在しない場合は None。
    """
    if downloads_dir is None:
        downloads_dir = Path.home() / "Downloads"
    else:
        downloads_dir = Path(downloads_dir)

    if not downloads_dir.exists():
        print(f"エラー: フォルダが存在しません: {downloads_dir}", file=sys.stderr)
        return None

    files = [f for f in downloads_dir.iterdir() if f.is_file()]

    if not files:
        print("ダウンロードフォルダにファイルがありません。", file=sys.stderr)
        return None

    return max(files, key=lambda f: f.stat().st_mtime)


def main() -> None:
    downloads_dir = sys.argv[1] if len(sys.argv) > 1 else None
    latest = find_latest_download(downloads_dir)

    if latest is None:
        sys.exit(1)

    print(latest)


if __name__ == "__main__":
    main()
