# SI 的 AI 工具選報

更新日期：2026-11-04（Asia/Taipei）

## 焦點

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 1 | [OpenAI：ChatGPT 與 Codex 進入工程設計流程](https://openai.com/index/accelerating-engineering-for-the-physical-world/) | OpenAI 於 11/3 分享模型協助 CAD、PCB 設計、製造圖、模擬與跨領域設計審查的內部及合作案例，並宣布與 Mazda 合作探索車輛氣動與撞擊安全設計。公告也坦言，原型距離製造仍需多輪檢查，模型未穩定掌握製造限制與組裝公差；文中效益和使用成長數據均由 OpenAI 提供。工程團隊可用受控任務測試幾何／電路正確性、製造可行性，以及人工修訂量。 |

## 選讀

| 排名 | 工具 | 更新與觀察 |
|---|---|---|
| 2 | [Google Classroom：教師指派 Guided Learning](https://blog.google/products-and-platforms/products/education/guided-learning-uk-japan/) | Google 於 11/3 宣布教師主導的 Guided Learning 全球開放至 Google Classroom：教師可依課程材料指派逐步引導活動，並查看學生互動洞察；同日也公布兩項教室研究。這項功能把 AI 輔助放進教師設定的教材與課程脈絡，實際使用仍受 Workspace for Education 帳戶、地區及管理設定影響。學校可先核對租戶是否已開放、教師能看到哪些互動資料，以及學生輸入內容如何處理。 |
| 3 | [Claude Messages API：Message Threads beta](https://platform.claude.com/docs/en/build-with-claude/message-threads) | Anthropic 11/2 的平台更新為 Messages API 加入 message threads beta；長對話後續請求只需送新增訊息，目標是減少傳輸與前置處理、讓長代理流程的首 token 延遲更穩定。Threads 最後使用後 5 分鐘即可能到期，最遲一小時刪除；內容暫存在記憶體、加密，但不符合 ZDR 或 HIPAA，應用端仍須保存完整對話並處理重播。導入前可比較長流程延遲與失效重試，並確認資料保留政策符合要求。 |

## 快覽

| 排名 | 工具 | 更新與觀察 |
|---|---|---|

## 趨勢

| 主題 | 關聯工具 | 一句話重點 | 驗證重點 |
|---|---|---|---|
| AI 從單輪回答走進有脈絡的長任務 | [ChatGPT 與 Codex 工程流程](#item-01) · [Classroom Guided Learning](#item-02) · [Message Threads](#item-03) | 三項更新都把 AI 放進持續進行的工作：專業設計、教師引導課程與長代理對話；成果因此更依賴明確脈絡、領域檢查和人工監督。 | 工程案例須檢查可製造性；Classroom 須確認帳戶與管理範圍；Threads 須測試重播、延遲及資料保留限制。 |

## 來源

- [OpenAI：Accelerating engineering for the physical world](https://openai.com/index/accelerating-engineering-for-the-physical-world/)
- [Google：Guided Learning research and new Google Classroom features](https://blog.google/products-and-platforms/products/education/guided-learning-uk-japan/)
- [Anthropic：Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview)
- [Anthropic：Message threads documentation](https://platform.claude.com/docs/en/build-with-claude/message-threads)
