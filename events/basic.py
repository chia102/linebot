from line_bot_api import *

def about_us_event(event):
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


# if __name__ == "__main__":
#     app.run()