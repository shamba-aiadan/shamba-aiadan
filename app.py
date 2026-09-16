from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/")
def home():
return "Shamba AI is running"

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
media_url = request.values.get("MediaUrl0", None)

resp = MessagingResponse()
msg = resp.message()

if media_url:
msg.body(
"Asante kwa kutuma picha!\n\n"
"Nimepokea picha ya mmea wako.\n"
"Kwa sasa niko katika hatua ya majaribio.\n\n"
"Thank you for the photo. Full diagnosis is coming soon."
)
else:
msg.body(
"Habari! Tuma picha ya jani la mmea ili niweze kukusaidia.\n\n"
"Hello! Please send a photo of a plant leaf so I can help you."
)

return str(resp)

if __name__ == "__main__":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
