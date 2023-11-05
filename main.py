from flask import Flask, render_template, request
import subprocess

app = Flask("Simpleオンライン環境")

@app.route("/")
def index():
    return render_template("index.html", code="print 'Hello, world'",reply="")

@app.route("/", methods=["POST"])
def execute():
    code = request.form.get("code")
    print(code)

    with open(r"C:\Users\admin\OneDrive\デスクトップ\プログラミング\Python\プログラム\Simpleオンライン環境\code.smp", mode="w", encoding="utf-8") as f:
        f.write(code)

    # 実行したいexeファイルのパス
    exe_path: str = r"C:\Users\admin\OneDrive\デスクトップ\プログラミング\Rust\インタプリタ\target\release\simple.exe"

    # コマンドライン引数のリスト
    args = [r"C:\Users\admin\OneDrive\デスクトップ\プログラミング\Python\プログラム\Simpleオンライン環境\code.smp"]

    # subprocess.runを使用してexeを実行
    result = subprocess.run([exe_path] + args, capture_output=True, text=True, encoding='utf-8')
    
    print(result.stdout)
    return render_template("index.html", code=code, reply = result.stdout)

app.run(host="127.0.0.1", port=8888, debug=True)