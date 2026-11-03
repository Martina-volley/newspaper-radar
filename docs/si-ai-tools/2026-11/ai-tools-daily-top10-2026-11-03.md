# SI 的 AI 工具選報

更新日期：2026-11-03（Asia/Taipei）

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [OpenAI LifeVal：評估 AI 能否完成日常任務](https://openai.com/index/lifeval/) | OpenAI 於 11/2 公開 LifeVal，涵蓋照護、健康、教育、家務、個人財務、購物與政府服務等真實生活情境，並列出 GPT‑6 Astra 在多項任務的成績。這是 OpenAI 自行設計與呈現的評測，不代表獨立驗證，也不等於一般使用者在不同地區、帳戶或工具權限下都能重現。可先看任務是否包含完整執行與人工確認，再用自己的常見流程檢查成功率、錯誤代價及所需介入。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [Google Cloud Model Armor：串流篩檢支援排除規則預覽](https://docs.cloud.google.com/model-armor/release-notes) | Google Cloud 於 11/2 將逐模板排除規則擴展至串流消毒預覽，可用字典或正規表示式調整提示注入／越獄與負責任 AI 篩檢的誤判；緩衝模式支援部分或完整比對，即時模式目前支援部分比對。排除規則會讓指定內容不再觸發相應篩檢，可能同時放過真正風險。部署前應以明確核准詞彙測試命中與未命中，並記錄被排除的案例；功能仍為 Preview。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 代理從「完成任務」走向「可控地完成」 | [LifeVal](#item-01) · [Model Armor](#item-02) | LifeVal 把評量拉到日常任務的實際完成度，Model Armor 則讓串流代理流程可調整安全篩檢；兩者分別補上效用衡量與執行防護。 | LifeVal 的分數需視為供應商自評；Model Armor 排除規則需以誤判和漏判案例回歸測試，並確認 Preview 限制。 |

## 來源

- [OpenAI：LifeVal](https://openai.com/index/lifeval/)
- [Google Cloud：Model Armor release notes](https://docs.cloud.google.com/model-armor/release-notes)
- [Google Cloud：Configure template-specific exclusion rules](https://docs.cloud.google.com/model-armor/configure-exclusion-rules)
