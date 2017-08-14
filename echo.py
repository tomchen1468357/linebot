from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('BEg+pXLIm6G6YKCFSNN7LEtG0KjAeQPzEvpJQ+2uGl6iaQ0H5WphX6ELhZUdTWG3uyL0o9MWUac5gHVuPfCJUVNLVy7PK09bTuCmkpUuqYzKk1YzjYOtX3tQYdzzJtfEYvJu7nn+EFQzuOtFyO/ZQQdB04t89/1O/w1cDnyilFU=)
handler = WebhookHandler('35df983db5d4d121cbac5b7aaffbb512')


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


@handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
