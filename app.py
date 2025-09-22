from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 初期ラベル（選択可能な言語）
LANG_LABELS = [
    "日本語", "英語", "中国語", "韓国語", "スペイン語", "フランス語", "イタリア語", "ドイツ語"
]

# 習得済み言語（メモリ保持、永続化は未実装）
learned_languages = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lang = request.form.get('language')
        if lang and lang not in learned_languages:
            learned_languages.append(lang)
        return redirect(url_for('index'))
    return render_template('index.html', labels=LANG_LABELS, learned=learned_languages)

if __name__ == '__main__':
    app.run(debug=True)
