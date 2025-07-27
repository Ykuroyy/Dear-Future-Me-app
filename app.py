from flask import Flask, render_template, request
from datetime import datetime
import random
import time
from messages import messages

app = Flask(__name__)

def get_daily_message():
    # 日付に基づいて一日中同じメッセージを表示
    today = datetime.now()
    day_of_year = today.timetuple().tm_yday
    year = today.year
    
    # 年と日付を組み合わせてインデックスを計算
    index = (year * 1000 + day_of_year) % len(messages)
    
    return messages[index]

def get_random_message():
    # 現在時刻をシードにしてランダムメッセージを取得
    random.seed(int(time.time() * 1000000))
    return random.choice(messages)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/message')
def message():
    today = datetime.now().strftime('%Y年%m月%d日')
    
    # ランダムパラメータがある場合はランダムメッセージを表示
    if request.args.get('random') == 'true':
        message = get_random_message()
    else:
        message = get_daily_message()
    
    return render_template('index.html', today=today, message=message)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)