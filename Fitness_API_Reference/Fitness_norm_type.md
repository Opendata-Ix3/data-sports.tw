---
title: Fitness Service RESTful API reference (Fitness Norm Type)

---

# Fitness Service RESTful API reference (Fitness Norm Type)

## 目錄
1. [概述](#概述)
2. [授權與認證](#授權與認證)
3. [API端點](#API)
4. [請求格式](#請求格式)
5. [回應格式](#回應格式)
6. [錯誤處理](#錯誤處理)
7. [使用範例](#使用範例)

## 概述
本指引提供如何與體適能 API 介接說明。透過此常模類型 API，開發者可以查詢全部的常模名稱和數量，以便後續使用類型名稱取得特定常模的資料。在此之前，開發者請先參考 Authorization 章節之說明完成授權與認證。

## 授權與認證
使用加值模組 API 之前，需要先取得授權 Token。所有 API 請求必須包含以下標頭：

- `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### API
向下述 API 端點發送 POST 請求以獲取 Token：
- URL: `<https://{domain}/fitness/norm/type`>
- 方法: `GET`
- 標頭: `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### 請求格式
- 請求參數: 無

### 回應格式
- 回應格式與內容:
  ```json
  {
    "code": 200,
    "message": "操作成功 (Operation Successfully)",
    "timestamp": 1724894747395,
    "size": 7,
    "data": [
        {
            "type": "Cardiovascular_Endurance",
            "desc": "心肺耐力"
        },
        {
            "type": "Flexibility",
            "desc": "柔軟度"
        },
        {
            "type": "Lower_Body_Fat",
            "desc": "下肢體脂肪"
        },
        {
            "type": "Muscle_Strength",
            "desc": "肌力"
        },
        {
            "type": "Trunk_Body_Fat",
            "desc": "軀幹體脂肪"
        },
        {
            "type": "Upper_Body_Fat",
            "desc": "上肢體脂肪"
        },
        {
            "type": "Waist_Hip_Ratio",
            "desc": "腰臀圍比"
        }
    ]
  }

### 錯誤處理
| 錯誤代碼 | 說明 | 可能原因 | 建議解決方案 |
| -------- | -------- | -------- | -------- |
| 401 | 未經授權 | 認證失敗 | 檢查帳號和密碼是否正確 |
| 404 | 資源不存在 | 無法找到請求資源 | 檢查URL是否有拼寫錯誤 |

### 使用範例
- 使用 Curl 查詢全部常模類型的指令如下:
```shell=
curl "https://{domain}/fitness/norm/type"
-H "accept: application/json" -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}"
```