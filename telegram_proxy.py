from flask import Flask, request, redirect, render_template_string
import os

app = Flask(__name__)

# Trang HTML đơn giản để chuyển hướng người dùng tới ứng dụng chính
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>NebulaChest Redirect</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            color: white;
        }
        .container {
            text-align: center;
            background-color: rgba(0, 0, 0, 0.5);
            padding: 2rem;
            border-radius: 10px;
            max-width: 600px;
            width: 90%;
        }
        h1 {
            color: #00b4d8;
        }
        p {
            margin: 1rem 0;
            line-height: 1.5;
        }
        .redirect-btn {
            display: inline-block;
            background-color: #00b4d8;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            margin-top: 1rem;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        .redirect-btn:hover {
            background-color: #0077b6;
        }
        .loader {
            border: 5px solid #f3f3f3;
            border-top: 5px solid #00b4d8;
            border-radius: 50%;
            width: 40px;
            height: 40px;
            animation: spin 1s linear infinite;
            margin: 20px auto;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>NebulaChest</h1>
        <div class="loader"></div>
        <p>Đang chuyển hướng đến NebulaChest Game...</p>
        <p>Token: {{ token }}</p>
        <a href="{{ redirect_url }}" class="redirect-btn">Nhấn vào đây nếu không tự động chuyển hướng</a>
    </div>
    <script>
        // Tự động chuyển hướng sau 2 giây
        setTimeout(() => {
            window.location.href = "{{ redirect_url }}";
        }, 2000);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    # Lấy token từ query string nếu có
    token = request.args.get('token', '')
    
    # URL đích để chuyển hướng (app chính chạy trên port 5000)
    # Chuyển hướng đến Replit URL
    redirect_url = f"https://workspace.mtykp8.repl.co?token={token}"
    
    # Trong môi trường phát triển, chuyển hướng đến localhost:5000
    if os.environ.get('FLASK_ENV') == 'development':
        redirect_url = f"http://localhost:5000?token={token}"
    
    # Trả về trang HTML với token và URL chuyển hướng
    return render_template_string(HTML_TEMPLATE, token=token, redirect_url=redirect_url)

if __name__ == '__main__':
    # Chạy Flask trên port 8080 để không xung đột với ứng dụng chính
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)