from flask import Flask, request, abort
from linebot import (LineBotApi, WebhookHandler, exceptions)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


line_bot_api = LineBotApi('mKAdfOUe4RhcJq/r7eo/thB1pq+P+2vr5jVVL7FYz5KgsxDUt5BVSTGDKHT515PCVsSFelbM4ZZvWmWcUDlCpCeofJrrlyZcXf4KXSjyJbYxtOknIAQQCR6Ce32uVrsOYRVi47zPmpTwA9Vx88SYzAdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('542f7955d3c281995cfc5a5693a5cb14')