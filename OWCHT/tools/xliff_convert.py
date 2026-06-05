#!/usr/bin/env python3
"""
Outer Wilds CHT Translation converter
1. Translation.txt → XLIFF 1.2  (for memoQ)
2. XLIFF 1.2 → Translation.txt  (rebuild after editing)

檔案位置：
  - OWCHT/Translations txt/translation.xliff    （Mode 1 生成，memoQ 匯入用）
  - OWCHT/Translations txt/translation_zho-TW.xliff  （memoQ 匯出，放這裡）
  - OWCHT/Translations txt/translation.txt      （Mode 2 生成，repo 版本）
  - mod 資料夾/Translation.txt                  （Mode 2 生成，本機測試用）
"""

import json
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

XLIFF_NS = 'urn:oasis:names:tc:xliff:document:1.2'

# tools/ 所在目錄（OWCHT/tools/）
TOOLS_DIR    = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT    = os.path.dirname(os.path.dirname(TOOLS_DIR))  # 往上兩層到 repo root
TRANS_DIR    = os.path.join(REPO_ROOT, 'OWCHT', 'Translations txt')
REPO_TXT     = os.path.join(TRANS_DIR, 'translation.txt')
LOCAL_CONFIG = os.path.join(TOOLS_DIR, 'local_config.json')


def load_mod_folder() -> str | None:
    """從 local_config.json 讀取 mod 資料夾路徑，不存在則回傳 None。"""
    if not os.path.exists(LOCAL_CONFIG):
        return None
    with open(LOCAL_CONFIG, encoding='utf-8') as f:
        cfg = json.load(f)
    return cfg.get('mod_folder')


def write_to(content: bytes, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'wb') as f:
        f.write(content)
    print(f"  → {path}")


# ── Mode 1: Translation.txt → XLIFF ──────────────────────────────────────────

def translation_to_xliff(src_path: str, dst_path: str):
    tree = ET.parse(src_path)
    root = tree.getroot()

    xliff = ET.Element('xliff', {
        'version': '1.2',
        'xmlns': XLIFF_NS,
    })
    file_el = ET.SubElement(xliff, 'file', {
        'original': 'translation.txt',
        'source-language': 'en',
        'target-language': 'zh-TW',
        'datatype': 'xml',
    })
    body = ET.SubElement(file_el, 'body')

    uid = [1]

    def add_unit(key_el, val_el, note_text):
        tu = ET.SubElement(body, 'trans-unit', {'id': str(uid[0])})
        ET.SubElement(tu, 'source').text = (key_el.text or '').strip()
        ET.SubElement(tu, 'target').text = (val_el.text or '').strip()
        ET.SubElement(tu, 'note').text = note_text
        uid[0] += 1

    for entry in root.findall('entry'):
        k, v = entry.find('key'), entry.find('value')
        if k is not None and v is not None:
            add_unit(k, v, 'entry')

    shiplog = root.find('table_shipLog')
    if shiplog is not None:
        for entry in shiplog.findall('TranslationTableEntry'):
            k, v = entry.find('key'), entry.find('value')
            if k is not None and v is not None:
                add_unit(k, v, 'shipLog')

    table_ui = root.find('table_ui')
    if table_ui is not None:
        for entry in table_ui.findall('TranslationTableEntryUI'):
            k, v = entry.find('key'), entry.find('value')
            if k is not None and v is not None:
                add_unit(k, v, 'ui')

    total = uid[0] - 1
    raw = ET.tostring(xliff, encoding='unicode')
    pretty = minidom.parseString(raw).toprettyxml(indent='  ', encoding='utf-8')
    write_to(pretty, dst_path)
    print(f"完成：{total} 個 segment")


# ── Mode 2: XLIFF → Translation.txt ──────────────────────────────────────────

def xliff_to_translation(xliff_path: str):
    """從 XLIFF 重建 Translation.txt，寫入 repo 路徑及 mod 資料夾（若設定）。"""
    xtree = ET.parse(xliff_path)
    xroot = xtree.getroot()

    units = []
    for tu in xroot.iter(f'{{{XLIFF_NS}}}trans-unit'):
        src  = tu.find(f'{{{XLIFF_NS}}}source')
        tgt  = tu.find(f'{{{XLIFF_NS}}}target')
        note = tu.find(f'{{{XLIFF_NS}}}note')
        units.append((
            src.text  if src  is not None else '',
            tgt.text  if tgt  is not None else '',
            note.text if note is not None else 'entry',
        ))

    if not units:  # fallback：無 namespace
        for tu in xroot.iter('trans-unit'):
            src  = tu.find('source')
            tgt  = tu.find('target')
            note = tu.find('note')
            units.append((
                src.text  if src  is not None else '',
                tgt.text  if tgt  is not None else '',
                note.text if note is not None else 'entry',
            ))

    if not units:
        print("錯誤：XLIFF 裡找不到任何 trans-unit，請確認格式正確。")
        sys.exit(1)

    root = ET.Element('TranslationTable_XML')
    shiplog_el = ET.Element('table_shipLog')
    ui_el      = ET.Element('table_ui')
    counts = {'entry': 0, 'shipLog': 0, 'ui': 0}

    for src_text, tgt_text, note in units:
        note = (note or 'entry').strip()
        if note == 'entry':
            e = ET.SubElement(root, 'entry')
            ET.SubElement(e, 'key').text   = src_text
            ET.SubElement(e, 'value').text = tgt_text
            counts['entry'] += 1
        elif note == 'shipLog':
            e = ET.SubElement(shiplog_el, 'TranslationTableEntry')
            ET.SubElement(e, 'key').text   = src_text
            ET.SubElement(e, 'value').text = tgt_text
            counts['shipLog'] += 1
        elif note == 'ui':
            e = ET.SubElement(ui_el, 'TranslationTableEntryUI')
            ET.SubElement(e, 'key').text   = src_text
            ET.SubElement(e, 'value').text = tgt_text
            counts['ui'] += 1

    root.append(shiplog_el)
    root.append(ui_el)

    raw    = ET.tostring(root, encoding='unicode')
    pretty = minidom.parseString(raw).toprettyxml(indent='  ', encoding='utf-8')

    total = sum(counts.values())
    print(f"完成：{total} 個 segment（entry {counts['entry']} / shipLog {counts['shipLog']} / ui {counts['ui']}）")

    # 寫入 repo 路徑
    write_to(pretty, REPO_TXT)

    # 寫入 mod 資料夾（若設定）
    mod_folder = load_mod_folder()
    if mod_folder:
        mod_txt = os.path.join(mod_folder, 'translation.txt')
        write_to(pretty, mod_txt)
    else:
        print(f"  （未設定 mod 資料夾，跳過。可在 tools/local_config.json 設定）")


# ── Main ──────────────────────────────────────────────────────────────────────

def prompt_path(label: str, default: str = None) -> str:
    hint = f"（直接 Enter → {default}）" if default else ""
    val = input(f"{label}{hint}: ").strip().strip('"').strip("'")
    return val if val else default

def main():
    print("=== Outer Wilds CHT Translation Converter ===")
    print("1. Translation.txt → XLIFF（匯入 memoQ）")
    print("2. XLIFF → Translation.txt（翻譯完回組）")
    choice = input("選擇 (1/2): ").strip()

    if choice == '1':
        default_src = REPO_TXT
        src = prompt_path("Translation.txt 路徑", default=default_src)
        default_dst = os.path.join(TRANS_DIR, 'translation.xliff')
        dst = prompt_path("輸出 XLIFF 路徑", default=default_dst)
        translation_to_xliff(src, dst)

    elif choice == '2':
        default_xliff = os.path.join(TRANS_DIR, 'translation_zho-TW.xliff')
        xliff = prompt_path("XLIFF 路徑", default=default_xliff)
        xliff_to_translation(xliff)

    else:
        print("無效選擇，請輸入 1 或 2。")
        sys.exit(1)

if __name__ == '__main__':
    main()
