from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def index():
    conn = sqlite3.connect("students.db")
    conn.execute("create table student(name text)")
    conn.close()
    return render_template('content.html', msg='DB and table created ')


@app.route('/insert')
def create_record():
    name = 'Leonardo Anjos'
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute('insert into student(name) values(?)', [name])
        cur.commit()

    return render_template('content.html', msg='Record inserted')


@app.route('/dynamic/<text>')
def dynamic_record():
    name = text
    with sqlite3.connect('students.db') as conn:
        cur = conn.cursor()
        cur.execute('insert into student(name) values(?)', [name])
        cur.commit()

    return render_template('content.html', msg='Record inserted')


@app.route('/select')
def select_all_records():
    with sqlite3.connect('students.db') as conn:
        conn.row_factory() = sqlite3.Row
        cur = conn.cursor()

        cur.execute("select * from student")
        rows = cur.fetchall()

    return render_template('content.html', rows_content=row)


app.run()
