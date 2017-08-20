import requests
import re
import random
import time
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__) # 傳入__name__初始化一個Flask實例
line_bot_api = LineBotApi('BEg+pXLIm6G6YKCFSNN7LEtG0KjAeQPzEvpJQ+2uGl6iaQ0H5WphX6ELhZUdTWG3uyL0o9MWUac5gHVuPfCJUVNLVy7PK09bTuCmkpUuqYzKk1YzjYOtX3tQYdzzJtfEYvJu7nn+EFQzuOtFyO/ZQQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('35df983db5d4d121cbac5b7aaffbb512')
client_id = 'YOUR_IMGUR_CLIENT_ID'
client_secret = 'YOUR_IMGUR__CLIENT_SECRET'
album_id = 'YOUR_IMGUR_ALBUM_ID'
API_Get_Image ='API_Get_Image'


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 200

def get_web_page(url):
    resp = requests.get(
        url=url,
        cookies={'over18': '1'}
    )
    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        #        return resp.text
        return resp.text

def money_J_U():
    allcash = []
    product = []
    dodo1 = []
    allshowcashbuy = []
    alltaxcashbuy = []
    allshowcashsell = []
    alltaxcashsell = []
    tax1 = []
    page = get_web_page('http://rate.bot.com.tw/xrt?Lang=zh-TW')
# print(page)
    butidodo = BeautifulSoup(page, 'html.parser')
# print(butidodo)
    dodo_find = butidodo.find_all("td", "rate-content-cash text-right print_hide")
# print(dodo_find)
    cash_doler = butidodo.find_all("div", "visible-phone print_hide")
# print(cash_doler)
    tax_find = butidodo.find_all("td", "rate-content-sight text-right print_hide")
#    print(tax_find)
    for cashs in cash_doler:
        wow = cashs.text.strip()
        allcash.append(wow)

    for tax in tax_find:
     #   print(dodo)
        tax2 = tax.text.strip()
        tax1.append(tax2)


# print(dodo_find)
    for dodo in dodo_find:
     #   print(dodo)
        do2 = dodo.text.strip()
        dodo1.append(do2)
#    print(dodo1)
#    print(tax1)
    for aa in range(len(allcash)):
        bb = aa * 2

        if allcash[aa] == "美金 (USD)" or allcash[aa] == "日圓 (JPY)":
            showcashbuy = dodo1[bb]
            taxcashbuy = tax1[bb]
            allshowcashbuy.append(showcashbuy)
            alltaxcashbuy.append(taxcashbuy)
            showcashsell = dodo1[bb + 1]
            taxcashsell = tax1[bb + 1]
            allshowcashsell.append(showcashsell)
            alltaxcashsell.append(taxcashsell)
    recodetime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    allcash11 = ["美金(USD)", "日圓(JPY)"]
    USD_NOW = '\n{} {} \n現金本行:買入{} 賣出{} \n即期本行:買入{} 賣出{}'.format(recodetime, allcash11[0], allshowcashbuy[0], allshowcashsell[0], alltaxcashbuy[0], alltaxcashsell[0])
    JPY_NOW = '\n{} {} \n現金本行:買入{} 賣出{} \n即期本行:買入{} 賣出{}'.format(recodetime, allcash11[1], allshowcashbuy[1], allshowcashsell[1], alltaxcashbuy[1], alltaxcashsell[1])
    JPYANDUSD = '{}\n{}'.format(USD_NOW, JPY_NOW)
    return JPYANDUSD


print()

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if event.message.text == "台銀即時匯率":
        content = money_J_U()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

    if event.message.text == "lativ打幾折":
        content = "抱歉目前尚未建置完成，敬請選擇其他選項"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "my protein打幾折":
        content = "抱歉目前尚未建置完成，敬請選擇其他選項"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "奇摩子電影":
        content = "抱歉目前尚未建置完成，敬請選擇其他選項"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text != "奇摩子電影":
    buttons_template = TemplateSendMessage(
        alt_text='目錄 template',
        template=ButtonsTemplate(
            title='選擇服務',
            text='請選擇',
            thumbnail_image_url='http://i.imgur.com/IHFI8zN.png',
            actions=[
                MessageTemplateAction(
                    label='台銀即時匯率',
                    text='台銀即時匯率'
                ),
                URITemplateAction(
                    label='lativ打幾折',
                    text='lativ打幾折'
                ),
                URITemplateAction(
                    label='my protein打幾折',
                    text='my protein打幾折'
                ),
                URITemplateAction(
                    label='奇摩子電影',
                    text='奇摩子電影'
                )
            ]
        )
    )
        return 0
    line_bot_api.reply_message(event.reply_token, buttons_template)


if __name__ == '__main__':
    app.run()
