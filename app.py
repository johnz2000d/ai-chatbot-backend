from flask import Flask, request, jsonify
from flask_cors import CORS  # 🔥 允许跨域请求 (CORS)

# 创建 Flask 应用
app = Flask(__name__)
CORS(app)  # ✅ 允许所有来源访问 Flask API

# 处理根路径的请求
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Hello from root!"})

# 处理 /chat 路由的 POST 请求
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json  # 获取 JSON 数据
    if not data or "message" not in data:
        return jsonify({"error": "Invalid request"}), 400  # 错误处理

    user_input = data["message"]
    return jsonify({"response": f"AI Response to: {user_input}"})

# 启动 Flask 应用（本地测试时使用）
if __name__ == "__main__":
    app.run(debug=True)
