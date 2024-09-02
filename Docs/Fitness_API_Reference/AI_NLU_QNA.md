---
title: Fitness Service RESTful API reference (AI NLU QNA)

---

# Fitness Service RESTful API reference (AI NLU QNA)

## 目錄
1. [概述](#概述)
2. [授權與認證](#授權與認證)
3. [API端點](#API)
4. [請求格式](#請求格式)
5. [回應格式](#回應格式)
6. [錯誤處理](#錯誤處理)
7. [使用範例](#使用範例)

## 概述
本指引提供如何與體適能 API 介接說明。透過此NLU 問答知識庫 API，輸入使用者的問題，可以取得知識庫中的答案。在此之前，開發者請先參考 Authorization 章節之說明完成授權與認證。

## 授權與認證
使用加值模組 API 之前，需要先取得授權 Token。所有 API 請求必須包含以下標頭：

- `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### API
向下述 API 端點發送 POST 請求以獲取 Token：
- URL: `<https://{domain}/ai/nlu/qna`
- 方法: `GET`
- 標頭: `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### 請求格式
- 請求格式與參數:
```shell=
https://{domain}/ai/nlu/qna?question={question}[&version=version]
```

| 名稱 | 類型 | 說明 | 備註 | 必要欄位 | 
| -------- | -------- | -------- | -------- | -------- |
| question | string | 問題 |  | 是 |
| version | string | API 版號(yyyy-MM-dd) | 無版號則使用預設版本 | 否 |

### 回應格式
- 回應格式與內容:
  ```json
  {
    "code": 200,
    "message": "操作成功 (Operation Successfully)",
    "timestamp": 1724983926884,
    "question": "初學者怎麼運動",
    "answers": [
      "初學者應該先從基礎動作開始，學習如何正確地執行各種鍛煉動作。建議從低強度的有氧運動（如散步或慢跑）開始，逐漸增加強度和時間。還應該包括力量訓練（如深蹲、伏地挺身）和柔韌性訓練（如瑜伽或伸展運動）。保持每週至少3-4次的鍛煉頻率，並確保有足夠的休息時間來恢復。"
    ]
  }

### 錯誤處理
| 錯誤代碼 | 說明 | 可能原因 | 建議解決方案 |
| -------- | -------- | -------- | -------- |
| 400 | 缺少參數 | 請求缺少必要參數 | 檢查參數是否完整 |
| 401 | 未經授權 | 認證失敗 | 檢查帳號和密碼是否正確 |
| 404 | 資源不存在 | 無法找到請求資源 | 檢查URL是否有拼寫錯誤 |

### 使用範例
- 使用 Curl 介接 API 的指令如下:
```shell=
curl -X GET "https://{domain}/ai/nlu/qna?question={question}&version=2024-08-15"
-H "accept: application/json" -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}"
```