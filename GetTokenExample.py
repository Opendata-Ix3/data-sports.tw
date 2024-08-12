# @title Get-Token-Example
# 預設在CoLab上執行
import requests
import json
#import matplotlib.pyplot as plt    # 用來畫圖的

#### =>> 開始使用前, 請記得設定您的帳號密碼
MY_MEMBER_NAME = "little test"    # 帳號
MY_PASSWORD = "big result"    # 密碼


#### =>> 查詢類別
#### 開始使用前, 請記得調整您想要查詢的類別名稱
main_type = "PhysicalFitness"    # 體適能: PhysicalFitness
type = "ResistanceTraining"    # 阻力訓練: ResistanceTraining
subtype = ""    # 可能沒有「子類型」
data_size = 100    # 每次查詢可以有 [100筆 | 1000筆 | 10000筆] 三種範圍



##################################################
### 上面的參數很重要 很重要 很重要
##################################################

# 定義 數據公益平臺網站的 API URL 根路徑
api_base_url = "https://api.data-sports.tw"


# 1. 進行登入動作
api_url_login = "/member/login"
my_account_info = {
    'membername': MY_MEMBER_NAME,
    'password': MY_PASSWORD
    }
#new_url = api_base_url + api_url_login
#print(new_url)

# 執行登入動作
response = requests.post(api_base_url + api_url_login, json = my_account_info)

result_login = None
# 1.1 檢查回應狀態碼
if response.status_code == 200:
    # 解析 JSON 回應
    result_login = response.json()

    # 展示回傳資料
    #print(result_login)    # 可不用顯示
else:
    print("呼叫 API 失敗，狀態碼：", response.status_code)
    exit(1)

# 1.2 登入成功, 取出toekn
my_login_toekn = result_login.get('data').get('token')
#print(myLoginToekn)
#myLoginToekn = result_login['token']
#print(myLoginToekn)


# 2. 呼叫查詢資料的API
# 2.1 準備參數
api_url = api_base_url + "/data/processed"
headers = {'Authorization': f"Bearer {my_login_toekn}"}
parameters = {'main_type': main_type, 'type': type, 'subtype': subtype, 'data_size': data_size}

# 執行查詢
response = requests.get(api_url, headers=headers, params=parameters)


# 2.2 檢查回應狀態碼
if response.status_code == 200:
    # 解析 JSON 回應
    data = response.json()

    # 展示回傳資料
    json_string = json.dumps(data['data']['data'], indent = 2)
    print("查詢結果：\n" + json_string)

    ### 要注意 download_count 的當天次數
    json_string = json.dumps(data['data']['download_count'], indent = 2)
    print("\n本月已查詢次數：" + json_string)
    print("\n本次查詢使用的token：" + my_login_toekn)
    print("\n")
else:
    print(f"Error: {response.status_code}")
    #print("呼叫 API 失敗，狀態碼：", response.status_code)



##################################################
### 上面的程式碼可以直接複製到coLab去執行
##################################################
### 下面的程式不重要
##################################################

### 不想執行測試程式, 可在此離開
exit(0)


##################################################
# 外部範例
# 定義 API URL
api_url = "https://jsonplaceholder.typicode.com/posts/1"

# 呼叫 API
response = requests.get(api_url)

# 檢查回應狀態碼
if response.status_code == 200:
    # 解析 JSON 回應
    data = response.json()

    # 展示回傳資料
    print(data)
else:
    print("呼叫 API 失敗，狀態碼：", response.status_code)