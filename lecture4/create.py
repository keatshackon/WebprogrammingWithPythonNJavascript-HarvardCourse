import os

from flask import Flask,render_template,request
from models import *

#creating application here!
app= Flask(__name__)

#connecting the database with url
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:9264@localhost:5432/aerolines'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)  #bind this application with database


def main():
    db.create_all()

if __name__=="__main__":
    with app.app_context():
        main()
