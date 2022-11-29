from flask import Flask , request , abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import(MessageEvent , TextMessage,TextSendMessage)

app = Flask(__name__)

access_token = ""
secret = ""

line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(secret)

@app.route("/callback" , methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body:" + body)

    try:
        handler.handle(body,signature)
    except InvalidSignatureError as e:
        print(e)
        abort(400)
    return "OK"


@handler.add(MessageEvent,message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )
#test
if __name__ == "__main__":
    app.run()