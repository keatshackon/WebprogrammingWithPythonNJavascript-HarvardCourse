from flask import Flask,render_template,request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:9264@localhost:5432/keats"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#connect Database to Application
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
    return render_template("index.html",flights = flights)

@app.route("/book",methods = ["POST"])
def book():
    name = request.form.get("name")
    if(name == ""):
        return render_template("error.html",message = "Please Enter Your Name! ")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html",message = "Invalid Flight Number")


    #make sure Flight exist
    flight = Flight.query.get(flight_id)
    if( flight is None):
        return render_template("error.html",message = "No Such Flight With This ID")

    #Add a passenger
    flight.add_passenger(name)
    # passenger = Passenger(name = name,flight_id = flight_id)
    # db.session.add(passenger)
    # db.session.commit()
    return render_template("successful.html")

@app.route("/flights")
def flights():
    """List Of All The Flights"""

    flights = Flight.query.all()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about a single flight."""

    # Make sure flight exists.
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message = "No such flight.")

    # Get all passengers.
    #passengers = Passenger.query.filter_by(flight_id = flight_id).all()
    #below line will fetch all the attributes of the passengers tables
    passengers = flight.passengers
    return render_template("flight.html", flight = flight, passengers = passengers)

@app.route("/flights")
def listFlight():
    return render_template("flights.html")

if __name__=="__main__":
    with app.app_context():
        app.run(debug = True)
