import os
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import io

app = Flask(__name__)
CORS(app)

PHOTO_FOLDER = os.path.join("server", "photo")


@app.route("/api/upload", methods=["POST"])
def upload():
    image = request.json.get("image")  # Lấy dữ liệu ảnh từ request

    # Tạo thư mục "photo" nếu chưa tồn tại
    if not os.path.exists(PHOTO_FOLDER):
        os.makedirs(PHOTO_FOLDER)

    # Tính số lượng file hiện có trong thư mục
    num_files = len(
        [
            f
            for f in os.listdir(PHOTO_FOLDER)
            if os.path.isfile(os.path.join(PHOTO_FOLDER, f))
        ]
    )

    # Lưu ảnh vào thư mục "photo" với tên là "photo_{num_files}.jpg"
    image_path = os.path.join(PHOTO_FOLDER, f"photo_{num_files}.jpg")

    format, imgstr = image.split(";base64,")
    b = io.BytesIO(base64.b64decode(imgstr))
    img_format = format.split("/")[-1]

    image_decoded = Image.open(b)

    # Save the image
    image_decoded.save(image_path, img_format)

    # In ra đường dẫn ảnh đã lưu
    print("Đường dẫn ảnh đã lưu:", image_path)

    # TODO: Xử lý dữ liệu ảnh theo yêu cầu

    # Ví dụ: Trả về kết quả là chuỗi "Success" cho ứng dụng ReactJS
    result = "Success"

    return jsonify(result=result)


if __name__ == "__main__":
    print("RUN")
    app.run(debug=True)
