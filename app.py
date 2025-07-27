from flask import Flask, render_template, request, session
from datetime import datetime
import random
import secrets
from messages import messages

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def get_daily_message():
    # 日付に基づいて一日中同じメッセージを表示
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    year = today.year
    
    # 年と日付を組み合わせてシード値を作成
    seed = year * 1000 + day_of_year
    
    # 一時的にランダムステートを保存
    state = random.getstate()
    random.seed(seed)
    
    # メッセージをランダムに選択
    message = random.choice(messages)
    
    # ランダムステートを復元
    random.setstate(state)
    
    return message

def get_random_message(exclude_message=None):
    # 完全にランダムなメッセージを選択（同じメッセージを除外）
    available_messages = [msg for msg in messages if msg != exclude_message]
    if len(available_messages) == 0:  # すべてのメッセージを見た場合
        available_messages = messages
    return random.choice(available_messages)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/message')
def message():
    today = datetime.now().strftime('%Y年%m月%d日')
    
    # ランダムモードかどうかを判定
    if request.args.get('random') == 'true':
        # セッションから前回のメッセージを取得
        last_message = session.get('last_message', '')
        # タイムスタンプを使って真のランダム性を確保
        import time
        random.seed(time.time())
        new_message = get_random_message(exclude_message=last_message)
        # 新しいメッセージをセッションに保存
        session['last_message'] = new_message
        current_message = new_message
    else:
        current_message = get_daily_message()
        session['last_message'] = current_message
    
    return render_template('index.html', today=today, message=current_message)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)