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



# 建立一個 Flask 應用實例

app = Flask(__name__)



# 初始化

configuration = Configuration(access_token='QT9ReFrJGz9b8qAVBEm3ZxdgdjEPHIQwK5DtdjUip+4b+wXikn1GPVIuCS52/3/OpA7ms7AnmE7oR2QAQu3j8PTqFDLDjXzRfVhBopH+8MF3UgB5zdsz2AT9OITU23yw+JqCDh3txDNReerSvCCc9QdB04t89/1O/w1cDnyilFU=')
# 設置 LINE Bot 的配置，這裡需要使用你的 Channel Access Token

handler = WebhookHandler('daa0c351de5006bd1cc25f1860985312')
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
    
    with ApiClient(configuration) as api_client:
        # 使用配置創建一個 ApiClient 實例

        line_bot_api = MessagingApi(api_client)
        # 使用 ApiClient 實例創建一個 MessagingApi 實例

        line_bot_api.reply_message_with_http_info(
        # 使用MessagingApi實例回覆消息
            ReplyMessageRequest(
            # 創建一個ReplyMessageRequest，包含reply_token和消息內容
                reply_token=event.reply_token,                
                messages=[TextMessage(text=event.message.text)]
                # 消息內容是用戶發送的相同文本消息，調用 reply_message_with_http_info 方法發送回覆消息
            )
        )

        

# 執行

if __name__ == "__main__":
    app.run()
    # 如果這個腳本是作為主程序運行，啟動Flask應用

