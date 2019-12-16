"""
line_broadcaster.py
[TESTING FUNCTION]
Connects to line's MessagingApi and broadcasts messages to user.
"""
from flask import (
    Blueprint, Flask, request, abort
)
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

# Reads tokens for line API access
from line_broadcaster.security_reader import SecurityReader
secretReader = SecurityReader()
lineApi = LineBotApi(secretReader.getToken())
lineWebhook = WebhookHandler(secretReader.getWebhookSecret())
secretReader.close()

bp = Blueprint("broadcaster", __name__, url_prefix="/line")

@bp.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    app.logger.info("Request body:" + body)

    #handle webhook body
    try:
        lineWebhook.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"

@lineWebhook.add(MessageEvent, message=TextMessage)
def handleMessage(event):
    lineApi.reply_message(
        event.reply_token,
        TextSendMessage(text="Your secret mix is: " + event.source.userId)
    )

def broadcastMessage(message="default message"):
    lineApi.broadcast(
        TextSendMessage(text=message)
    )

def multiCastMessage():
    lineApi.multicast(
        ["--aluminum--"],
        TextSendMessage(text="You've received some Secret Chikuma Mix.")
    )

if __name__ == "__main__":
    broadcastMessage()
