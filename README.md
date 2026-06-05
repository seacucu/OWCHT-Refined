![Outer Wilds 精修繁體](https://github.com/user-attachments/assets/32af0cff-e9ce-4d8e-9230-a58ad1f17b23)

# Outer Wilds 台灣繁中模組

將遊戲語言從簡體中文替換為台灣繁體中文，並修正字型缺字問題。

## 功能

- 完整繁體中文翻譯（對話、星際日誌、UI）
- 改用動態字型，解決部分漢字無法顯示的問題
- 支援從外部 `Translation.txt` 讀取翻譯，免重新打包即可更新文字

## 安裝方式

透過 [Outer Wilds Mod Manager](https://outerwildsmods.com/mod-manager/) 一鍵安裝。

## 自訂翻譯

如果你想修改翻譯文字，可以直接編輯 mod 資料夾內的 `Translation.txt`，重啟遊戲即生效，不需要重新 build mod。

## 翻譯說明

本模組的翻譯基於 puffbro 的版本，以[繁化姬](https://zhconvert.org/)進行簡繁轉換後，再逐句人工校正。

主要修正項目包括：

- **字形替換**：`麽→麼`、`里→裡`、`恒→恆`、`余→餘`、`覆→複/覆`（依語義區分）、`炮→砲`、`巖→岩`、`卷→捲` 等簡繁差異
- **用語在地化**：`估計→恐怕/我想`（語氣詞）、`咱們→我們`、`制作→製作`、`志→誌`（日誌）等
- **人名重譯**：部分角色名依英文原文重新音譯，如 `所萊內姆→索拉農`、`費利克斯→菲力斯`、`斯拜爾→史派爾`、`埃文斯→艾凡斯`、`奧埃諾→歐伊諾` 等

## 致謝

- 原始繁中翻譯：[puffbro/outer-wilds-traditional-chinese-translation](https://github.com/puffbro/outer-wilds-traditional-chinese-translation)
- 簡繁轉換工具：[繁化姬](https://zhconvert.org/)
- 韓文翻譯原始碼：[milesand](https://github.com/milesand)（puffbro 的原始來源）

## License

MIT
