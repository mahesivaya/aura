import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import psycopg2
from flask_login import UserMixin
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import declarative_base
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"


db = SQLAlchemy(app)


class Another(db.Model):
    ###User model### 
    __tablename__ = 'another'
    #unique user id 
    id = db.Column(db.Integer, primary_key=True)
    #Each field is specified as a class attribute, 
    #and each attribute maps to a database column.
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    #make a relationship with 'Posts' model 
    user_blog = db.relationship('Posts', backref='list', lazy=True)

    def __init__(self, username, email, password):
        self.username = username 
        self.email = email
        self.password = password
        
    def __repr__(self):
        return '<User {}>'.format(self.username)

from sqlalchemy import create_engine
# for postgreSQL database credentials can be written as 
user = 'postgres'
password = 'postgres'
host = 'localhost'
port = '5432'
database = 'postgres'
# for creating connection string
url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
# SQLAlchemy engine
engine = create_engine(url)
# you can test if the connection is made or not
try:
    with engine.connect() as url:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')

Base = declarative_base()

# class Article(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer(), primary_key=True)
#     slug = Column(String(100), nullable=False, unique=True)
#     title = Column(String(100), nullable=False)
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#     content = Column(Text)
#     author_id = Column(Integer(), ForeignKey('authors.id'))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(80), nullable=False)



Base.metadata.create_all(engine)


def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='postgres',
                            user='postgres',
                            password='postgres')
    return conn


@app.route('/')
def main():
    return render_template('mainpage.html')


@app.route('/register/')
def register():
    return render_template('register.html')



@app.route('/login/')
def login():
    return render_template('login.html')



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
    app.run(debug=True, host='0.0.0.0', port=4000)