import json

from flask import (
    Flask, request, abort
)
# 從 Flask 庫導入 Flask 應用、請求對象和 abort 函式，用於處理 HTTP 請求。

from linebot.v3 import (
    WebhookHandler
)
# 從 LINE Bot SDK 導入 WebhookHandler，用於處理 Webhook 事件。

from linebot.v3.exceptions import (
    InvalidSignatureError
)
# 從 LINE Bot SDK 導入 InvalidSignatureError，用於處理無效簽名的異常情況。

from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
# 從 LINE Bot SDK 導入配置、API 客戶端、消息 API、回覆消息請求和文本消息，用於與 LINE 消息 API 進行互動。

from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
# 從 LINE Bot SDK 導入消息事件和文本消息內容，用於處理 Webhook 事件中的消息。

import requests

# 建立一個 Flask 應用實例

app = Flask(__name__)



# 初始化
with open("..\local\config.json") as f:
    config = json.load(f)
# print(config)

configuration = Configuration(access_token=config["channel_access_token"])
# 設置 LINE Bot 的配置，這裡需要使用你的 Channel Access Token

handler = WebhookHandler(config["channel_secret"])
# 建立一個 Webhook 處理器實例，這裡需要使用你的 Channel Secret



# 定義 Flask 應用中的一個路由，該路由處理來自 "/callback" URL 的 POST 請求

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    # 獲取請求標頭中的'X-Line-Signature'值，用於驗證請求是否合法

    body = request.get_data(as_text=True)
    # 獲取請求的主體內容並將其作為文本格式

    app.logger.info("Request body: " + body)
    # 記錄請求主體內容到應用的日誌中

    try:
        handler.handle(body, signature)
        # 使用 WebhookHandler 處理請求主體和簽名
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        # 如果簽名無效，記錄錯誤信息到日誌中
        abort(400)
        # 返回 400 錯誤響應

    return 'OK'
    # 如果處理成功，返回'OK'



# 這個裝飾器告訴 handler 在接收到 MessageEvent 且消息內容為 TextMessageContent 時調用 handle_message 函數

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    print(event.message.text)
    
    with ApiClient(configuration) as api_client:
        # 使用配置創建一個 ApiClient 實例

        line_bot_api = MessagingApi(api_client)
        # 使用 ApiClient 實例創建一個 MessagingApi 實例

        line_bot_api.reply_message_with_http_info(
        # 使用MessagingApi實例回覆消息
            ReplyMessageRequest(
            # 創建一個ReplyMessageRequest，包含reply_token和消息內容
                reply_token=event.reply_token,                
                messages=[TextMessage(text=replyMessage(event.message.text))]
                # 消息內容是用戶發送的相同文本消息，調用 reply_message_with_http_info 方法發送回覆消息
            )
        )



# 自動回覆家長的請假訊息

def replyMessage(user_message_lower):
    if "請假" in user_message_lower:
        reply_message = "收到，請協助提醒孩子要再帶假卡和請假證明，來完成請假手續。謝謝您！"
    elif "請病假" in user_message_lower:
        reply_message = "收到，請協助提醒孩子要再帶假卡和公私立醫療院所的就醫證明，來完成請假手續。謝謝您！"
    elif "請事假" in user_message_lower:
        reply_message = "收到，請協助提醒孩子要再帶假卡，來完成請假手續。謝謝您！"
    elif "請喪假" in user_message_lower:
        reply_message = "收到，請協助提醒孩子要再帶假卡和訃聞，來完成請假手續。謝謝您！"
    elif "請生理假" in user_message_lower:
        reply_message = "收到，請協助提醒孩子要再帶假卡，來完成請假手續。謝謝您！"
    else:
        return
        # reply_message = user_message_lower
    line_notify_image(user_message_lower)
    return  reply_message



# 透過 token 轉傳訊息到私人帳號或群組

def line_notify_image(message):
    # token = config.TOKEN
    token = config["line_notify_token"]

    # 要發送的訊息
    # message = '這是用 Python 發送的訊息與圖片'

    # HTTP 標頭參數與資料
    headers = {"Authorization": "Bearer " + token}
    data = {'message': message}

    # 要傳送的圖片檔案
    # image = open(f'/workspace/{msg_id}.jpg', 'rb')
    # files = {'imageFile': image}

    # 以 requests 發送 POST 請求
    requests.post("https://notify-api.line.me/api/notify",
                  headers=headers, data=data)
                #   headers=headers, data=data, files=files)



# 執行

if __name__ == "__main__":
    app.run()
    # 如果這個腳本是作為主程序運行，啟動Flask應用

