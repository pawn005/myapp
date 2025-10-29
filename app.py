from flask import Flask, render_template

app = Flask(__name__)

# トップページ：100個のボタンを表示
@app.route('/')
def index():
    pages = [f"{i:03}" for i in range(100)]  # 000〜099
    return render_template('index.html', pages=pages)

# 各ページ（000〜099）
@app.route('/page/<page_id>')
def page(page_id):
    return render_template('page.html', page_id=page_id)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
