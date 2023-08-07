from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('mKAdfOUe4RhcJq/r7eo/thB1pq+P+2vr5jVVL7FYz5KgsxDUt5BVSTGDKHT515PCVsSFelbM4ZZvWmWcUDlCpCeofJrrlyZcXf4KXSjyJbYxtOknIAQQCR6Ce32uVrsOYRVi47zPmpTwA9Vx88SYzAdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('542f7955d3c281995cfc5a5693a5cb14')

@app.route("/callback", methods=['POST'])
def callback():

    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(100)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    emoji = [
            {
                "index": 0,
                "productId": "52118404015980943a",
                "emojId":"225"

            },
            {
                "index": 17,
                "productId": "5ac2213e040ab15980c9b447",
                "emojId":"005"   
            }
        ]
    
    text_message = TemplateSendMessage ( text='''$ Master Finance $
Hello! 您好，歡迎您成為 Master Finance 的好友!

我是Master 財經小幫手

-這裡有股票，匯率資訊哦~
-直接點選下方功能選單
-期待您的光臨!''', emojis= emoji)
    
    sticker_message = StickerMessage(
        package_id='8522',
        sticker_id='16581271'
    )



if __name__ == "__main__":
    app.run()