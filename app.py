
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('14lwoYOIHNqC5CF2ApytmWiy3yNBkrXM/gbG5JL7h26on8dfsxpAuJhgWflBxZz92jYG3uvzqg3w7rObwKWsFZo1Jy4cHMT6pdkQEAKIeBz8QT84L2kRIygzni3ZQi2zPFpOG3kS+lF/poqwODq1ngdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('1e6c02a27c29d2ff7943b8ed4ea3a0c8')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=str(event.message.text+'XD'))
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8081))
    app.run(host='0.0.0.0', port=port)
