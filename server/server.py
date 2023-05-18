from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
import base64
import datetime

app = Flask(__name__)
CORS(app)

app = Flask(__name__)


@app.route("/", methods=["OPTIONS", "POST"])
@cross_origin()
def save_image():
    data = request.get_json()

    if "image" not in data:
        return jsonify({"error": "No image provided."}), 400

    img_data = data["image"].split(",")[1]
    img_bytes = base64.b64decode(img_data)

    if not os.path.exists("photos"):
        os.makedirs("photos")

    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpg"
    with open("photos/" + filename, "wb") as f:
        f.write(img_bytes)

    return jsonify({"message": "Image saved."}), 200


if __name__ == "__main__":
    app.run(debug=True)
