rom flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
# Get the incoming message
incoming_msg = request.values.get("Body", "").lower()
media_url = request.values.get("MediaUrl0", None)

resp = MessagingResponse()
msg = resp.message()

if media_url:
# Temporary simple reply (we will upgrade the diagnosis later)
msg.body(
"Asante kwa kutuma picha!\n\n"
"Nimepokea picha ya mmea wako.\n"
"Kwa sasa niko katika hatua ya majaribio.\n\n"
"Hivi karibuni nitakuwa naweza kugundua magonjwa ya mimea na kukupa ushauri.\n\n"
"Thank you for the photo! The system is under testing. Full diagnosis coming soon."
)
else:
msg.body(
"Habari! Tuma picha ya jani la mmea ili niweze kukusaidia.\n\n"
"Hello! Please send a photo of a plant leaf so I can help you."
)

return str(resp)

if __name__ == "__main__":
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
