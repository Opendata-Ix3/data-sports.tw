---
title: Fitness Service RESTful API reference (Fitness Norm Data)

---

# Fitness Service RESTful API reference (Fitness Norm Data)

## 目錄
1. [概述](#概述)
2. [授權與認證](#授權與認證)
3. [API端點](#API)
4. [請求格式](#請求格式)
5. [回應格式](#回應格式)
6. [錯誤處理](#錯誤處理)
7. [使用範例](#使用範例)

## 概述
本指引提供如何與體適能 API 介接說明。透過此常模資料 API，開發者可以查詢取得特定體適能常模的資料，以及各常模百分比等級區間的上、下限數值。在此之前，開發者請先參考 Authorization 章節之說明完成授權與認證。

## 授權與認證
使用加值模組 API 之前，需要先取得授權 Token。所有 API 請求必須包含以下標頭：

- `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### API
向下述 API 端點發送 POST 請求以獲取 Token：
- URL: `<https://{domain}/fitness/norm/data`>
- 方法: `GET`
- 標頭: `Authorization: Bearer {YOUR_ACCESS_TOKEN}`

### 請求格式
- 請求格式與參數:
```shell=
https://{domain}/fitness/norm/data?age={age}&gender={gender}&type={type}[&measurement={measurement}]
```

| 名稱 | 說明 | 描述 | 必要欄位 | 
| -------- | -------- | -------- | -------- |
| age | 年齡 |   | 是 |
| gender | 性別 | M: 男, F: 女 | 是 |
| type | 體適能類型 | 由 norm type 取得 | 是 | 
| measurement | 量測值 |   | 否 |

### 回應格式
- 回應格式與內容:
  ```json
  {
    "code": 200,
    "message": "操作成功 (Operation Successfully)",
    "timestamp": 1724980958719,
    "size": 1,
    "data": [
        {
            "type": "Flexibility",
            "age_group": "23-24",
            "gender": "Male",
            "lower_limit": 20.31,
            "upper_limit": 26.83,
            "percentile": "20-40"
        }
    ]
  }

### 錯誤處理
| 錯誤代碼 | 說明 | 可能原因 | 建議解決方案 |
| -------- | -------- | -------- | -------- |
| 400 | 缺少參數 | 請求缺少必要參數 | 檢查參數是否完整 |
| 401 | 未經授權 | 認證失敗 | 檢查帳號和密碼是否正確 |
| 404 | 資源不存在 | 無法找到請求資源 | 檢查URL是否有拼寫錯誤 |

### 使用範例
- 使用 Curl 查詢全部常模類型的指令如下:
```shell=
curl "https://{domain}/fitness/norm/data?age=23&gender=M&type=Flexibility&measurement=22"
-H "accept: application/json" -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}"
```