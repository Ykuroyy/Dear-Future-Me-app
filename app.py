from flask import Flask, render_template, request
from datetime import datetime
import random
from messages import messages

app = Flask(__name__)

def get_daily_message():
    # 日付に基づいて一日中同じメッセージを表示
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    year = today.year
    
    # 年と日付を組み合わせてシード値を作成
    seed = year * 1000 + day_of_year
    random.seed(seed)
    
    # メッセージをランダムに選択
    message = random.choice(messages)
    
    return message

def get_random_message():
    # 完全にランダムなメッセージを選択
    return random.choice(messages)

@app.route('/')
def index():
    today = datetime.now().strftime('%Y年%m月%d日')
    
    # クエリパラメータでランダム表示かどうかを判定
    if request.args.get('random') == 'true':
        message = get_random_message()
    else:
        message = get_daily_message()
    
    return render_template('index.html', today=today, message=message)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)