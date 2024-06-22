from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from sqlalchemy.sql import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"
db = SQLAlchemy(app)


# from sqlalchemy import create_engine
# engine = create_engine("postgresql://postgres:postgres@localhost:5432/postgres")
# insp = inspect(engine)
# print(insp.get_table_names())

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    bio = db.Column(db.Text)

    def __repr__(self):
        return f'<Student {self.firstname}>'
    



# from app import db
# from sqlalchemy.dialects.postgresql import JSON


# class Result(db.Model):
#     __tablename__ = 'results'

#     id = db.Column(db.Integer, primary_key=True)
#     url = db.Column(db.String())
#     result_all = db.Column(JSON)
#     result_no_stop_words = db.Column(JSON)

#     def __init__(self, url, result_all, result_no_stop_words):
#         self.url = url
#         self.result_all = result_all
#         self.result_no_stop_words = result_no_stop_words

#     def __repr__(self):
#         return '<id {}>'.format(self.id)




from sqlalchemy import inspect
