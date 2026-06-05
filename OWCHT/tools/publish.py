#!/usr/bin/env python3
"""
Outer Wilds CHT - 翻譯發佈腳本
1. 選擇 XLIFF 檔案，轉換並套用到 mod 資料夾
2. （選擇性）bump 版本號、commit、push
"""

import json
import os
import subprocess
import sys
import webbrowser
import tkinter as tk
from tkinter import filedialog

# 路徑設定
TOOLS_DIR   = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT   = os.path.dirname(os.path.dirname(TOOLS_DIR))
TRANS_DIR   = os.path.join(REPO_ROOT, 'OWCHT', 'Translation_Text')
MANIFEST    = os.path.join(REPO_ROOT, 'OWCHT', 'manifest.json')
REPO_TXT    = os.path.join(TRANS_DIR, 'translation.txt')
GITHUB_ACTIONS_URL = 'https://github.com/Seacucu/OWCHT-Refined/actions'

sys.path.insert(0, TOOLS_DIR)
from xliff_convert import xliff_to_translation


def pick_xliff() -> str:
    print("正在開啟檔案選擇視窗，請切換到瀏覽視窗選擇 XLIFF 檔案...")
    root = tk.Tk()
    root.withdraw()
    root.lift()
    root.attributes('-topmost', True)
    path = filedialog.askopenfilename(
        title='選擇 XLIFF 檔案',
        initialdir=TRANS_DIR,
        filetypes=[('XLIFF 檔案', '*.xliff'), ('所有檔案', '*.*')],
    )
    root.destroy()
    return path


def read_version() -> str:
    with open(MANIFEST, encoding='utf-8') as f:
        return json.load(f)['version']


def write_version(version: str):
    with open(MANIFEST, encoding='utf-8') as f:
        data = json.load(f)
    data['version'] = version
    with open(MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write('\n')
    print(f"  manifest.json 版本號更新為 {version}")


def run(cmd: list[str]):
    result = subprocess.run(cmd, cwd=REPO_ROOT, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"錯誤：{' '.join(cmd)}")
        print(result.stderr)
        sys.exit(1)
    if result.stdout.strip():
        print(result.stdout.strip())


def do_apply():
    xliff_path = pick_xliff()
    if not xliff_path:
        print("未選擇檔案，結束。")
        sys.exit(0)
    if not os.path.exists(xliff_path):
        print(f"找不到檔案：{xliff_path}")
        sys.exit(1)
    print(f"選擇檔案：{xliff_path}\n")
    print("── 轉換中 ──")
    xliff_to_translation(xliff_path)
    print("\n✔ 翻譯已套用到 mod 資料夾。\n")


def do_publish():
    # 版本號
    current = read_version()
    print(f"目前版本號：{current}")
    new_version = input("新版本號（Enter 保留原版本）: ").strip()
    if not new_version:
        new_version = current
    else:
        write_version(new_version)

    # commit message 備註
    note = input("備註（Enter 略過）: ").strip()
    msg = f"Update translation to {new_version}"
    if note:
        msg += f": {note}"

    # git add / commit / push
    print(f"\n── Git ──")
    print(f"commit message: {msg}")
    files = [os.path.relpath(REPO_TXT, REPO_ROOT)]
    if new_version != current:
        files.append(os.path.relpath(MANIFEST, REPO_ROOT))
    run(['git', 'add'] + files)
    run(['git', 'commit', '-m', msg])
    run(['git', 'push'])

    print(f"\n✔ 已 push！")
    if new_version != current:
        print("  版本號有變動，GitHub Actions 會建立新的 draft release。")
    else:
        print("  版本號未變動，不會產生新的 release。")

    ans = input("\n要開啟 GitHub Actions 頁面嗎？(y/n): ").strip().lower()
    if ans == 'y':
        webbrowser.open(GITHUB_ACTIONS_URL)


def main():
    print("=== Outer Wilds CHT 翻譯發佈腳本 ===\n")
    print("1. 套用翻譯（選 XLIFF → 轉換 → 複製到 mod 資料夾）")
    print("2. 發佈（commit + push，不重新轉換）")
    choice = input("\n選擇 (1/2): ").strip()

    if choice == '1':
        do_apply()
        print("啟動遊戲測試看看吧！")

    elif choice == '2':
        print()
        do_publish()

    else:
        print("無效選擇。")
        sys.exit(1)


if __name__ == '__main__':
    main()
