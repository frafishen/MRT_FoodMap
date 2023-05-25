from flask import Flask, request, jsonify
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#password = quote_plus("xX@0180368905")
password = quote_plus("00000")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/mrt_foodmap'  # 你的資料庫URI
db = SQLAlchemy(app)



class Person(db.Model):
    __tablename__ = 'Person'  # 確保table name與你的SQL table相同
    PersonID = db.Column(db.String(50), primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(12), nullable=False)
    Location = db.Column(db.String(50))

class Station(db.Model):
    __tablename__ = 'Station'  # 確保table name與你的SQL table相同
    StationID = db.Column(db.String(50), primary_key=True)
    Name = db.Column(db.String(50), nullable=False)

    def __init__(self, StationID, Name):
        self.StationID = StationID
        self.Name = Name

class Event(db.Model):
    __tablename__ = 'Event'
    EventID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    P1_ID = db.Column(db.String(50), nullable=False)
    P2_ID = db.Column(db.String(50), nullable=False)
    Time = db.Column(db.DateTime, nullable=False)
    FoodType = db.Column(db.String(50), nullable=False)
    StationID = db.Column(db.String(50), nullable=False)

    def __init__(self, P1_ID, P2_ID, Time, FoodType, StationID):
        self.P1_ID = P1_ID
        self.P2_ID = P2_ID
        self.Time = Time
        self.FoodType = FoodType
        self.StationID = StationID

CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})



@app.route('/api/person', methods=['GET'])
def get_persons():
    persons = db.session.query(Person).all()
    persons_list = [{'PersonID': person.PersonID, 'Name': person.Name, 'Password': person.Password, 'Location': person.Location} for person in persons]
    return jsonify(persons_list)

@app.route('/api/person/<id>', methods=['GET'])
def get_person(id):
    person = db.session.get(Person, id) 
    if person is None:
        return 'No such person', 404
    person_dict = {'PersonID': person.PersonID, 'Name': person.Name, 'Password': person.Password, 'Location': person.Location}
    return jsonify(person_dict)



@app.route('/api/station', methods=['GET'])
def get_stations():
    stations = db.session.query(Station).all()
    stations_list = [{'StationID': station.StationID, 'Name': station.Name} for station in stations]
    return jsonify(stations_list)

@app.route('/api/station/<id>', methods=['GET'])
def get_station(id):
    station = db.session.get(Station, id) 
    if station is None:
        return 'No such station', 404
    station_dict = {'StationID': station.StationID, 'Name': station.Name} 
    return jsonify(station_dict)



@app.route('/api/event', methods=['GET'])
def get_events():
    events = db.session.query(Event).all()
    events_list = [{'EventID': event.EventID, 'P1_ID': event.P1_ID, 'P2_ID': event.P2_ID, 'Time': event.Time, 'FoodType': event.FoodType, 'StationID':event.StationID} for event in events]
    return jsonify(events_list)

@app.route('/api/event/<id>', methods=['GET'])
def get_event(id):
    event = db.session.get(Event, id) 
    if event is None:
        return 'No such event', 404
    event_dict = {'EventID': event.EventID, 'P1_ID': event.P1_ID, 'P2_ID': event.P2_ID, 'Time': event.Time, 'FoodType': event.FoodType, 'StationID':event.StationID}
    return jsonify(event_dict)



if __name__ == '__main__':
    app.run(port=5000)