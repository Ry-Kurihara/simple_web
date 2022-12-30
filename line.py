from flask import request, abort
import os, sys 
from sqlalchemy import create_engine 
import param_store as ps

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

from flask import Blueprint 
from flask import current_app as app 
line = Blueprint('line', __name__)

YOUR_CHANNEL_ACCESS_TOKEN = ps.get_parameters('/line/message_api/line_channel_access_token')
YOUR_CHANNEL_SECRET = ps.get_parameters('/line/message_api/line_channel_secret')
HEROKU_POSTGRES_URL = ps.get_parameters('/heroku/postgres_url')

# engine = create_engine(HEROKU_POSTGRES_URL)
line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@line.route("/callback", methods=['POST'])
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))