from models import *
from flask import Flask,render_template,request

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:9264@localhost:5432/aerolines"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights = Flight.query.all()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__=="__main__":
    with app.app_context():
        main()
