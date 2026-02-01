from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>工业温度转换网页版</title>
    <style>
        body { font-family: Arial; text-align: center; padding-top: 50px; background-color: #f4f7f6; }
        .container { display: inline-block; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input { padding: 10px; border: 1px solid #ddd; border-radius: 5px; }
        button { padding: 10px 20px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🌡️ 工业监控系统网页版</h2>
        <form method="POST">
            <input type="text" name="celsius" placeholder="输入摄氏度" required>
            <button type="submit">计算华氏度</button>
        </form>
        
        {% if fahrenheit %}
            <h3 style="color: #e74c3c;">换算结果: {{ fahrenheit }} F</h3>
            {% if fahrenheit >= 212 %}
                <p style="color: red; font-weight: bold;">⚠️ 警报：检测到沸腾！</p>
            {% endif %}
        {% endif %}
    </div>
</body>
</html>
""" 

@app.route("/", methods=["GET", "POST"])
def index():
    fahrenheit = None
    if request.method == "POST":
        celsius_val = request.form.get("celsius")
        try:
            fahrenheit = float(celsius_val) * 1.8 + 32
        except ValueError:
            fahrenheit = "输入错误"
    return render_template_string(HTML_TEMPLATE, fahrenheit=fahrenheit)

if __name__ == "__main__":
    app.run(debug=True)