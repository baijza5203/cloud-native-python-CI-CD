from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud-Native DevSecOps Demo</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #0f172a;
            color: #e5e7eb;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .box {
            background: #020617;
            padding: 40px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 0 20px rgba(56,189,248,0.4);
        }
        h1 { color: #38bdf8; }
        .status {
            margin-top: 20px;
            padding: 10px 20px;
            background: #22c55e;
            color: #022c22;
            border-radius: 999px;
            font-weight: bold;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>🚀 DevSecOps CI/CD Demo</h1>
        <p>Python Flask app deployed on Kubernetes</p>
        <p>Jenkins · Docker · AWS ECR · Kubernetes</p>
        <div class="status">Application Running Successfully</div>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
