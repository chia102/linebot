from line_bot_api import *
from events.basic import *

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

def push_msg(event,msg):
    try:
        user_id =event.source.user_id
        line_bot_api.push_message(user_id,TemplateSendMessage(text=msg))
    except:
        room_id = event.source.room_id
        line_bot_api.push_message(room_id,TemplateSendMessage(text=msg))

def Usage(event):
    push_msg(event,"  🙂🙂 查詢方法 🙂🙂  \
             \n☢小幫手可以查詢油價➡匯率➡股價\
             \n\
             \n☢油價通知➡➡➡書入查詢油價\
             \n☢匯率通知➡➡➡書入查詢匯率\
             \n☢匯率兌換➡➡➡書入換匯USD/TWD\
             \n☢股價查詢➡➡➡輸入#股票代號")    