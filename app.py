from flask import Flask, render_template, request, jsonify, url_for
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import json

app = Flask(__name__)

# 🔸 モデル読み込み（初回だけ数秒かかります）
model_name = "sonoisa/t5-base-japanese"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

@app.route('/')
def index():
    buttons = [{"id": f"btn{i}", "url": url_for('page', num=i)} for i in range(100)]
    buttons_json = json.dumps(buttons)
    return render_template('index.html', buttons_json=buttons_json)

@app.route('/page/<int:num>')
def page(num):
    return render_template('page.html', page_id=num)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"result": "テキストを入力してください。"})

    # 🔸 日本語T5による要約
    input_text = "要約: " + text
    inputs = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=100, min_length=10, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return jsonify({"result": summary})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)