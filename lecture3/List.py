import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session


engine = create_engine("postgresql://postgres:9264@localhost:5432/keats")

db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.")

if __name__ == '__main__':
    main()
