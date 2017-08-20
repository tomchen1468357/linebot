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
    ''''
    if event.message.text == "PTT 表特版 近期大於 10 推的文章":
        content = ptt_beauty()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "來張 imgur 正妹圖片":
        client = ImgurClient(client_id, client_secret)
        images = client.get_album_images(album_id)
        index = random.randint(0, len(images) - 1)
        url = images[index].link.replace('http', 'https')
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "隨便來張正妹圖片":
        image = requests.get(API_Get_Image)
        url = image.json().get('Url')
        image_message = ImageSendMessage(
            original_content_url=url,
            preview_image_url=url
        )
        line_bot_api.reply_message(
            event.reply_token, image_message)
        return 0
    if event.message.text == "近期熱門廢文":
        content = ptt_hot()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "即時廢文":
        content = ptt_gossiping()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "近期上映電影":
        content = movie()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "科技新報":
        content = technews()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "PanX泛科技":
        content = panx()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "開始玩":
        buttons_template = TemplateSendMessage(
            alt_text='開始玩 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/xQF5dZT.jpg',
                actions=[
                    MessageTemplateAction(
                        label='新聞',
                        text='新聞'
                    ),
                    MessageTemplateAction(
                        label='電影',
                        text='電影'
                    ),
                    MessageTemplateAction(
                        label='看廢文',
                        text='看廢文'
                    ),
                    MessageTemplateAction(
                        label='正妹',
                        text='正妹'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "新聞":
        buttons_template = TemplateSendMessage(
            alt_text='新聞 template',
            template=ButtonsTemplate(
                title='新聞類型',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/vkqbLnz.png',
                actions=[
                    MessageTemplateAction(
                        label='蘋果即時新聞',
                        text='蘋果即時新聞'
                    ),
                    MessageTemplateAction(
                        label='科技新報',
                        text='科技新報'
                    ),
                    MessageTemplateAction(
                        label='PanX泛科技',
                        text='PanX泛科技'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "電影":
        buttons_template = TemplateSendMessage(
            alt_text='電影 template',
            template=ButtonsTemplate(
                title='服務類型',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/sbOTJt4.png',
                actions=[
                    MessageTemplateAction(
                        label='近期上映電影',
                        text='近期上映電影'
                    ),
                    MessageTemplateAction(
                        label='eyny',
                        text='eyny'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "看廢文":
        buttons_template = TemplateSendMessage(
            alt_text='看廢文 template',
            template=ButtonsTemplate(
                title='你媽知道你在看廢文嗎',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/ocmxAdS.jpg',
                actions=[
                    MessageTemplateAction(
                        label='近期熱門廢文',
                        text='近期熱門廢文'
                    ),
                    MessageTemplateAction(
                        label='即時廢文',
                        text='即時廢文'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
    if event.message.text == "正妹":
        buttons_template = TemplateSendMessage(
            alt_text='正妹 template',
            template=ButtonsTemplate(
                title='選擇服務',
                text='請選擇',
                thumbnail_image_url='https://i.imgur.com/qKkE2bj.jpg',
                actions=[
                    MessageTemplateAction(
                        label='PTT 表特版 近期大於 10 推的文章',
                        text='PTT 表特版 近期大於 10 推的文章'
                    ),
                    MessageTemplateAction(
                        label='來張 imgur 正妹圖片',
                        text='來張 imgur 正妹圖片'
                    ),
                    MessageTemplateAction(
                        label='隨便來張正妹圖片',
                        text='隨便來張正妹圖片'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0
''''
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
    line_bot_api.reply_message(event.reply_token, buttons_template)


if __name__ == '__main__':
    app.run()
