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
            "index":0,
            "porductId": "6359",
            "emojiId": "11069851",
        },
        {
            "index": 17,
            "porductId": "5ac2213e040ab15980c9b447",
            "emojiId": "006",
        },
    ]
    test_message = TextSendMessage(text='''$ Master Finance $
    Hello! 歡迎加入財經小幫手''',emoji=emoji)
    sticker_message = StickerSendMessage(
        package_id="8522",
        sticker_id="16581271",
        )
    line_bot_api.reply_message(
        event.reply_token,
        [test_message,sticker_message])
    # message = TextSendMessage(text=event.message.text)
    # line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()