import sqlite3

def init_db():
    # 连接到 SQLite 数据库（如果不存在会自动创建）
    conn = sqlite3.connect('campus_cats.db')
    cursor = conn.cursor()

    # 创建猫咪档案表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nickname TEXT NOT NULL,
            gender TEXT,
            personality TEXT,
            location TEXT,
            image_url TEXT
        )
    ''')

    # 创建打卡记录表
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS checkins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cat_id INTEGER,
            user_name TEXT,
            checkin_type TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (cat_id) REFERENCES cats (id)
        )
    ''')

    # 插入几条测试数据 (对应你 HTML 里的数据)
    cursor.execute("INSERT INTO cats (nickname, gender, personality, location, image_url) VALUES ('大橘', 'male', '亲人', '图书馆', 'd52d7bb9336778f016db84fa8947a51b.jpg')")
    cursor.execute("INSERT INTO cats (nickname, gender, personality, location, image_url) VALUES ('奶牛', 'male', '粘人', '体育馆', '641e61d1488213e1bae2aaa5da70a4a0.jpg')")
    cursor.execute("INSERT INTO cats (nickname, gender, personality, location, image_url) VALUES ('警长', 'female', '高冷', 'A座', 'b9231616b36dee649e581e02b89f5419.jpg')")

    conn.commit()
    conn.close()
    print("数据库初始化成功！已生成 campus_cats.db 文件。")

if __name__ == '__main__':
    init_db()