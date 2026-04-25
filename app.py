from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

# 获取数据库连接的辅助函数
def get_db_connection():
    conn = sqlite3.connect('campus_cats.db')
    conn.row_factory = sqlite3.Row # 让查询结果可以像字典一样访问
    return conn

# ================= 页面路由 (对接你的 HTML) =================

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/list.html')
def cat_list():
    return render_template('list.html')

@app.route('/detail.html')
def detail():
    return render_template('detail.html')

@app.route('/check-in.html')
def check_in():
    return render_template('check-in.html')

@app.route('/stats.html')
def stats():
    return render_template('stats.html')

@app.route('/profile.html')
def profile():
    return render_template('profile.html')

# ================= API 接口 (供进阶功能调用) =================

# 示例：获取所有猫咪数据的接口
@app.route('/api/cats', methods=['GET'])
def get_cats():
    conn = get_db_connection()
    cats = conn.execute('SELECT * FROM cats').fetchall()
    conn.close()
    # 将 SQLite 数据转换为 JSON 格式返回
    return jsonify([dict(row) for row in cats])

if __name__ == '__main__':
    # 开启 debug 模式，修改代码后自动重启
    app.run(debug=True, port=5000)