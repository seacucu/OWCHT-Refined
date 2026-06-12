![Outer Wilds 精修繁體](https://github.com/user-attachments/assets/32af0cff-e9ce-4d8e-9230-a58ad1f17b23)

[繁體中文](#繁體中文) | [English](#english)

---

<a id="繁體中文"></a>

# Outer Wilds 台灣繁中模組

為遊戲新增獨立的「**正體中文**」語言選項，提供台灣用語習慣的完整繁體中文翻譯。

## 功能

- 在語言選單新增獨立的「正體中文」選項，**不佔用、不覆蓋**任何原有語言
- 完整翻譯：對話、星際日誌、UI、《眼之回音》DLC
- 譯文與遊戲現行版本（1.1.16）文本完全同步
- 採用動態字型（Noto Sans TC），徹底解決缺字問題

## 前置需求

本模組基於 [Interplanetary Polyglot（xen.LocalizationUtility）](https://github.com/xen-42/outer-wilds-localization-utility) 框架。
透過 Mod Manager 安裝時會**自動帶入**前置模組，無需手動處理。

## 安裝方式

**方法一（推薦）**：透過 [Outer Wilds Mod Manager](https://outerwildsmods.com/mod-manager/) 直接搜尋並安裝。

**方法二（手動）**：
1. 安裝前置模組 [Interplanetary Polyglot](https://outerwildsmods.com/mods/interplanetarypolyglot/)
2. 從 [Releases](../../releases) 下載 zip，解壓縮後將資料夾放入 `OuterWildsModManager\OWML\Mods\`

安裝後啟動遊戲，至「音訊與語言」設定中選擇「正體中文」。

## 自訂翻譯

模組資料夾內的 `Translation.xml` 即為翻譯本體，直接編輯後重啟遊戲即生效，無需重新 build。

## 翻譯說明

- **2.0 起**：自英文原文全文重譯，以統一術語表維持譯名一致性，並經人工逐句校對。
- **1.x**：基於 puffbro 的版本，以[繁化姬](https://zhconvert.org/)簡繁轉換後人工校正。

主要特色：

- **台灣用語**：遣詞用字以台灣習慣為準（如「日誌」「製作」「我們」）
- **譯名統一**：人名、地名、專有名詞依術語表統一，部分角色名依原文重新音譯
  （如 `索拉農`、`菲力斯`、`史派爾`、`艾凡斯`、`歐伊諾`）
- **正字標準**：`麼`、`裡`、`恆`、`餘`、`砲`、`岩`、`捲` 等字形依台灣正字使用

## 致謝

- 語言框架：[xen-42/outer-wilds-localization-utility](https://github.com/xen-42/outer-wilds-localization-utility)
- 原始繁中翻譯：[puffbro/outer-wilds-traditional-chinese-translation](https://github.com/puffbro/outer-wilds-traditional-chinese-translation)
- 簡繁轉換工具：[繁化姬](https://zhconvert.org/)
- 韓文翻譯原始碼：[milesand](https://github.com/milesand)（puffbro 的原始來源）

## License

MIT

---

<a id="english"></a>

# Outer Wilds Traditional Chinese (Taiwan) Mod

Adds a standalone "正體中文" (Traditional Chinese) language option to the game, with a complete translation localized for Taiwan.

## Features

- Adds Traditional Chinese as a **new language option** — does not replace or occupy any existing language
- Full coverage: dialogue, ship log, UI, and the *Echoes of the Eye* DLC
- Text fully synchronized with the current game version (1.1.16)
- Dynamic font (Noto Sans TC) eliminates missing-character issues

## Requirements

Built on the [Interplanetary Polyglot (xen.LocalizationUtility)](https://github.com/xen-42/outer-wilds-localization-utility) framework.
The dependency is **installed automatically** when using the Mod Manager.

## Installation

**Option 1 (recommended):** Install via [Outer Wilds Mod Manager](https://outerwildsmods.com/mod-manager/).

**Option 2 (manual):**
1. Install the prerequisite mod [Interplanetary Polyglot](https://outerwildsmods.com/mods/interplanetarypolyglot/)
2. Download the zip from [Releases](../../releases), extract it, and place the folder into `%appdata%\OuterWildsModManager\OWML\Mods\`

After installation, launch the game and select「正體中文」under Audio & Language settings.

## Custom Translation

`Translation.xml` in the mod folder is the translation itself — edit it directly and restart the game to apply. No rebuild needed.

## Translation Notes

- **Since 2.0**: fully retranslated from the English original, with a glossary ensuring consistent terminology, reviewed sentence by sentence.
- **1.x**: based on puffbro's translation, converted via [zhconvert.org](https://zhconvert.org/) and manually corrected.

Highlights:

- **Taiwan-style wording** throughout
- **Consistent terminology**: character and place names re-transliterated from the English originals (e.g. Solanum, Feliks, Spire, Avens, Oeno)
- **Standard Taiwan glyphs** for regional character variants

## Credits

- Localization framework: [xen-42/outer-wilds-localization-utility](https://github.com/xen-42/outer-wilds-localization-utility)
- Original Traditional Chinese translation: [puffbro/outer-wilds-traditional-chinese-translation](https://github.com/puffbro/outer-wilds-traditional-chinese-translation)
- Simplified-to-Traditional converter: [zhconvert.org](https://zhconvert.org/)
- Korean translation source: [milesand](https://github.com/milesand) (puffbro's original base)

## License

MIT
