import os
from flask import Flask, render_template, request, url_for, redirect
import psycopg2


app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user='postgres',
                            password='postgres')
    return conn



@app.route('/home/')
def home():
    return render_template('home.html')




@app.route('/getallpersons/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM aurapatients;')
    names = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', names=names)


@app.route('/')
def main():
    return render_template('mainpage.html')



@app.route('/login/')
def login():
    return render_template('login.html')





@app.route('/addperson/', methods=('GET', 'POST'))
def addpeople():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        age = request.form['age']
        phonenumber = request.form['phonenumber']
        address = request.form['address']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO aurapatients (firstname, lastname, age, address, phonenumber)'
                    'VALUES (%s, %s, %s, %s, %s)',
                    (firstname, lastname, age, address, phonenumber))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
        
    return render_template('addperson.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)