from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/")
def home():
return """
<html>
<body style="font-family: Arial; padding: 20px;">
<h2>Shamba AI</h2>
<p>Upload a plant leaf photo.</p>
<form action="/diagnose" method="post" enctype="multipart/form-data">
<input type="file" name="photo" accept="image/*" required>
<br><br>
<button type="submit">Check plant</button>
</form>
</body>
</html>
"""

@app.route("/diagnose", methods=["POST"])
def diagnose():
photo = request.files.get("photo")
if not photo:
return "Please upload a photo."

return """
<html>
<body style="font-family: Arial; padding: 20px;">
<h2>Shamba AI</h2>
<p>Photo received.</p>
<p>Diagnosis is not ready yet. This is the test page.</p>
<p><a href="/">Upload another photo</a></p>
</body>
</html>
"""

if __name__ == "__main__":
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
