from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    buttons = [{"id": f"btn{i}", "url": url_for('page', num=i)} for i in range(100)]
    buttons_json = json.dumps(buttons)
    return render_template('index.html', buttons_json=buttons_json)

@app.route('/page/<int:num>')
def page(num):
    return render_template('page.html', page_id=num)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
