import requests
import re
import random
import time
from bs4 import BeautifulSoup
from flask import Flask, request, abort
# from imgurpython import ImgurClient
from linebot import (
	LineBotApi, WebhookHandler
	)
from linebot.exceptions import (
	InvalidSignatureError
	)
from linebot.models import *

# app = Flask(__name__)
line_bot_api = LineBotApi('BEg+pXLIm6G6YKCFSNN7LEtG0KjAeQPzEvpJQ+2uGl6iaQ0H5WphX6ELhZUdTWG3uyL0o9MWUac5gHVuPfCJUVNLVy7PK09bTuCmkpUuqYzKk1YzjYOtX3tQYdzzJtfEYvJu7nn+EFQzuOtFyO/ZQQdB04t89/1O/w1cDnyilFU=')
# handler = WebhookHandler('YOUR_CHANNEL_SECRET')
# client_id = 'YOUR_IMGUR_CLIENT_ID'
# client_secret = 'YOUR_IMGUR__CLIENT_SECRET'
# album_id = 'YOUR_IMGUR_ALBUM_ID'
# API_Get_Image ='API_Get_Image'
# @app.route("/callback", methods=['POST'])

# def callback():
#     # get X-Line-Signature header value
#     signature = request.headers['X-Line-Signature']

#     # get request body as text
#     body = request.get_data(as_text=True)
#     # print("body:",body)
#     app.logger.info("Request body: " + body)

#     # handle webhook body
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 200
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='習包子!'))
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='大撒幣!'))
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='大撒幣!'))
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='大撒幣!'))
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='大撒幣!'))
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='大撒幣!'))
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='大撒幣!'))
line_bot_api.push_message('U6e4177deca4c8e4be1f5f1446fd86836', TextSendMessage(text='大撒幣!'))



