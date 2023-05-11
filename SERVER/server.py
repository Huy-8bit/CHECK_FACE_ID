import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/upload", methods=["POST"])
def upload():
    image = request.json.get("image")  # Lấy dữ liệu ảnh từ request

    # Tạo thư mục "photo" nếu chưa tồn tại
    if not os.path.exists("photo"):
        os.makedirs("photo")

    # Lưu ảnh vào thư mục "photo"
    image_path = os.path.join("photo", "image.jpg")
    with open(image_path, "wb") as f:
        f.write(image.encode())

    # In ra đường dẫn ảnh đã lưu
    print("Đường dẫn ảnh đã lưu:", image_path)

    # TODO: Xử lý dữ liệu ảnh theo yêu cầu

    # Ví dụ: Trả về kết quả là chuỗi "Success" cho ứng dụng ReactJS
    result = "Success"

    return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=True)
