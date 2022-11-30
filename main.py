import os

from flask import Flask , request , abort , render_template
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import(MessageEvent , TextMessage,TextSendMessage)

app = Flask(__name__)

access_token = "RKS7MyLnXBnWvEAGPPIwNIDc6Q3pxAGrkuVN5mGkmhd1I1rKNW0ajCNTkB/hUqsW1Yk14FkpSHJsTGMwVYzv18RkRzdskWayAOlcsub3Or8nQpOKqG0KZ5rn6nfS4bTbt7VEZTpxTKNfLPQLrTgIgwdB04t89/1O/w1cDnyilFU="
secret = "159067c8686f57c9bcd3a3a34a3045b1"

line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(secret)

@app.route("/" , methods=["GET"])
def hello():
    return render_template("index.html")

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
    text = "https://liff.line.me/1657699545-5nm7xM1P"
    line_bot_api.reply_message(
        event.reply_token,
        # TextSendMessage(text=event.message.text)
        TextSendMessage(text=text)
    )
#test
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))