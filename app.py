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
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


if __name__ == "__main__":
    app.run()