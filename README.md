# newspaper-radar

AI 日報的公開存檔，依刊物及月份分類。

- [你的AI觀察雷達](docs/ai-radar/INDEX.md)
- [SI 的 AI 工具選報](docs/si-ai-tools/INDEX.md)
- [AI 資訊安全報](docs/ai-security/INDEX.md)

內容保留各期原始發布版本；文中來源與發布狀態以當期查核時間為準。

## 封面目錄自動更新

封面 `index.html` 的刊物目錄（各月期數、連結、期數統計與「閱讀最新一期」按鈕）由 `scripts/update_index.py` 依 `docs/` 內的 HTML 檔重新產生，只改寫 `<!-- CATALOG:…:START -->`／`<!-- CATALOG:…:END -->` 標記之間的內容與上述數字、連結，其餘版面不動。

```sh
python3 scripts/update_index.py          # 依 docs/ 更新 index.html
python3 scripts/update_index.py --check  # 只檢查；需要更新時以非零狀態結束
```

推送到 `main` 且有 `docs/**` 變更時，GitHub Actions（`.github/workflows/update-index.yml`）會自動執行腳本；若 `index.html` 有變更，便以 github-actions[bot] 提交 `chore: 更新封面目錄 [skip ci]` 並推回 `main`。
