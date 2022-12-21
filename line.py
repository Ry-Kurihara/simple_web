# from flask import request, abort
# import os, sys 
# from sqlalchemy import create_engine 
# import param_store as ps

# from app import app

# from linebot import (
#     LineBotApi, WebhookHandler
# )
# from linebot.exceptions import (
#     InvalidSignatureError
# )

# from linebot.models import (
#     MessageEvent, TextMessage, TextSendMessage,
# )

# YOUR_CHANNEL_ACCESS_TOKEN = ps.get_parameters('/line/message_api/line_channel_access_token')
# YOUR_CHANNEL_SECRET = ps.get_parameters('/line/message_api/line_channel_secret')
# HEROKU_POSTGRES_URL = ps.get_parameters('/heroku/postgres_url')
# engine = create_engine(HEROKU_POSTGRES_URL)
# line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
# handler = WebhookHandler(YOUR_CHANNEL_SECRET)

# @app.route("/callback", methods=['POST'])
# def callback():
#     # get X-Line-Signature header value: signatureは意味不明な文字列
#     signature = request.headers['X-Line-Signature']

#     # get request body as text: bodyはjson形式
#     body = request.get_data(as_text=True)
#     app.logger.info("Request body: " + body)

#     # handle webhook body: エラーメッセージを出力したくない場合tryでくるむ？ TODO: 後で調べる
#     try:
#         handler.handle(body, signature)
#     except InvalidSignatureError:
#         abort(400)

#     return 'OK'

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     line_bot_api.reply_message(
#         event.reply_token,
#         TextSendMessage(text=event.message.text))