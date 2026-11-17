# SI 的 AI 工具選報

更新日期：2026-11-17（Asia/Taipei）

觀察窗口：2026-11-16。今日核對到兩項新模型發布；規格與效能數字以官方說明為準，實際表現仍需自行測試。

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [Qwen4-Max：旗艦多模態模型正式推出](https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen4-max?_p_lc=1) | 阿里巴巴於 11/16 發布 Qwen4-Max，官方列出的規格包括 2.4 兆總參數、每 token 啟用 710 億參數，以及 100 萬 token 上下文，支援文字、影像與影片理解、深度推理、工具呼叫和結構化輸出；Alibaba Cloud Model Studio 文件也列出國際部署。阿里稱其在內部 Work360 任務集較前代少用 35% token、單任務成本降低約 60%，並報告多項基準成績；這些是供應商公布的評測，不能直接推論到自家工作負載。開發團隊可先確認區域與 API 可用性，再以固定的程式、文件及多模態任務比較準確度、延遲和總成本。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [Tencent Hy4 flash：面向日常工作流程的低成本模型](https://www.tencent.com/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows/) | 騰訊於 11/16 發布 Hy4 flash，官方規格為 2,240 億總參數、每 token 啟用 120 億參數，支援多模態輸入與最高 100 萬 token 上下文；列出的 API 價格約為每百萬輸入 token 0.07 美元、輸出 0.281 美元。模型已接入 WorkBuddy、騰訊雲 TokenHub 等服務。騰訊稱其內部 WorkIndex 的單任務成本低於數個比較模型，但該測試由廠商設計，不能視為獨立效能結論。適合先用常見辦公任務驗證文件、簡報與表格品質，並一併量測錯誤修正時間、延遲及實際帳單。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| 旗艦能力與日常成本開始分層 | [Qwen4-Max](#item-01) · [Tencent Hy4 flash](#item-02) | Qwen4-Max 主打複雜推理與多模態工作，Hy4 flash 則把重心放在日常任務的速度與成本；選型應依任務難度和實測總成本分流，而非只看參數規模或廠商基準。 | 用同一組工作樣本比較正確率、完成時間、重試與人工修正成本；另核對部署區域、輸入資料處理方式及 API 實際費率。 |

## 來源

- [Alibaba Cloud：Alibaba Unveils Qwen4-Max（2026-11-16）](https://www.alibabacloud.com/en/press-room/alibaba-unveils-qwen4-max?_p_lc=1)
- [Alibaba Cloud Model Studio：Qwen4-Max model documentation（2026-11-16）](https://www.alibabacloud.com/help/en/model-studio/qwen4-max)
- [Tencent：Tencent Launches Hy4 flash（2026-11-16）](https://www.tencent.com/tencent-launches-hy4-flash-to-power-high-speed-cost-efficient-ai-deployment-for-everyday-workflows/)
- [Tencent：Hy4 flash model overview and evaluation](https://hy.tencent.ai/research/hy4-flash)
