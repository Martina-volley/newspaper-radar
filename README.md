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

### 自動更新與發布（GitHub Actions）

推送到 `main` 且變更了 `docs/**`、`index.html`、`scripts/update_index.py` 或 workflow 本身時（也可在 Actions 頁面手動 Run workflow），`.github/workflows/update-index.yml` 會依序執行：

1. **update-catalog**：以最新的 `main` 執行腳本；若 `index.html` 有變更，便以 github-actions[bot] 提交 `chore: 更新封面目錄 [skip ci]` 並推回 `main`（推送失敗會重新抓取最新 `main` 再產生，最多 5 次）。
2. **pages-source**：讀取 GitHub Pages 的發布來源。
3. **deploy**：來源為「GitHub Actions」時，以當下最新的 `main` 建置只含 `index.html` 與 `docs/` 的網站並發布到 GitHub Pages。

### 一次性設定：把 Pages 來源改成 GitHub Actions

請依下列順序操作（需由 repo 擁有者手動設定）：

1. 先合併加入此 workflow 的 PR。
2. 開啟 <https://github.com/Martina-volley/newspaper-radar/settings/pages>，在 **Build and deployment → Source** 選擇 **GitHub Actions**。GitHub 可能會推薦範本 workflow，不需要新增。
3. 到 **Actions → 更新封面目錄並發布 Pages → Run workflow**（分支選 `main`）手動執行一次，確認 `deploy` job 成功，網站顯示最新一期。

在完成第 2 步之前，Source 仍是「Deploy from a branch」：目錄照常更新並提交，`pages-source` job 會顯示警告並請求一次分支重建，`deploy` job 則會略過。請勿在合併前先切換 Source，否則在 workflow 上線前，新推送都不會發布。
