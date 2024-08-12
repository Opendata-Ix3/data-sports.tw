# 運動數據公益平臺 data-sports.tw 開發者專區

## 取得 API Token 的範例
### 執行說明
- 預設在CoLab上執行
    > **所以還沒有提供venv與requirements.txt等設定說明**
- 輸出
    - 查詢結果
    - 本月剩餘的查詢次數
    - Token字串
#### 需自行填入的參數
1. 自己的帳號、密號(例如下面...)
```
MY_MEMBER_NAME = "little test"    # 帳號
MY_PASSWORD = "big result"    # 密碼
```

2. 想要查詢的數據類別(例如下面...)
```
main_type = "PhysicalFitness"    # 體適能: PhysicalFitness
type = "ResistanceTraining"    # 阻力訓練: ResistanceTraining
subtype = ""    # 可能沒有「子類型」
data_size = 100    # 每次查詢可以有 [100筆 | 1000筆 | 10000筆] 三種範圍
```