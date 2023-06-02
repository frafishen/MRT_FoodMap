from flask import Flask, request, jsonify
from urllib.parse import quote_plus
# from flask_sqlalchemy import SQLAlchemy,text, or_, and_
from sqlalchemy.sql.expression import between
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, or_, and_

import random
from datetime import datetime, timedelta


# password = quote_plus("xX@0180368905")
# password = quote_plus("00000")
password = quote_plus("221003red")

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

class FavoriteList(db.Model):
    __tablename__ = 'FavoriteList'
    FListID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PersonID = db.Column(db.String(50), nullable=False)
    StoreID = db.Column(db.String(50), nullable=False)
    # PersonID = db.Column(db.String(50), db.ForeignKey('person.PersonID'), nullable=False)
    # StoreID = db.Column(db.String(50), db.ForeignKey('store.StoreID'), nullable=False)
    # person = db.relationship('person', foreign_keys=[PersonID])
    # store = db.relationship('store', foreign_keys=[StoreID])

    def __init__(self, PersonID, StoreID):
        self.PersonID = PersonID
        self.StoreID = StoreID

class Store(db.Model):
    __tablename__ = 'Store'
    StoreID = db.Column(db.String(50), primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Location = db.Column(db.String(50), nullable=False)
    Category = db.Column(db.String(50), nullable=False)
    URL = db.Column(db.String(50), nullable=False)
    Distance = db.Column(db.String(50), nullable=False)

    def __init__(self, StoreID, Name, Location, Category, URL, Distance):
        self.StoreID = StoreID
        self.Name = Name
        self.Location = Location
        self.Category = Category
        self.URL = URL
        self.Distance = Distance

CORS(app)
# CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route("/api/login/<id>/<password>", methods=["GET"])
def login(id, password):
    person = db.session.query(Person).filter_by(PersonID=id, Password=password).first()
    if person is None:
        return 'No such person', 404
    person_dict = {'PersonID': person.PersonID, 'Name': person.Name, 'Password': person.Password, 'Location': person.Location}
    return jsonify(person_dict)

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

# add station, need to add stationID and name
@app.route('/api/addStation', methods=['POST'])
def add_station():
    response_object = {'status': 'success'}
    try:
        _json = request.json
        print(request.json)
        _stationID = _json['StationID']
        _name = _json['Name']
        if _stationID and _name and request.method == 'POST':
            sql = text("INSERT INTO Station(StationID, Name) VALUES(:stationID, :name)")
            data = {"stationID": _stationID, "name": _name}
            db.session.execute(sql, data)
            db.session.commit()
            response_object['message'] = 'Station added!'
            return jsonify(response_object)
        else:
            response_object['message'] = 'Invalid data'
            response_object['status'] = 'failed'
            return jsonify(response_object)
    except Exception as e:
        response_object['error'] = str(e)
        response_object['status'] = 'failed'
        app.logger.error(str(e))
        return jsonify(response_object)
    
# delete station, need to add stationID
@app.route('/api/deleteStation', methods=['POST'])
def delete_station():
    response_object = {'status': 'success'}
    try:
        _json = request.json
        _stationID = _json['StationID']
        if _stationID and request.method == 'POST':
            sql = text("DELETE FROM Station WHERE StationID = :stationID")
            data = {"stationID": _stationID}
            db.session.execute(sql, data)
            db.session.commit()
            response_object['message'] = 'Station deleted!'
            return jsonify(response_object)
        else:
            response_object['message'] = 'Invalid data'
            response_object['status'] = 'failed'
            return jsonify(response_object)
    except Exception as e:
        response_object['error'] = str(e)
        response_object['status'] = 'failed'
        app.logger.error(str(e))
        return jsonify(response_object)
    
@app.route('/api/addPerson', methods=['POST'])
def add_person():
    response_object = {'status': 'success'}
    try:
        _json = request.json
        _PersonID = _json['PersonID']
        _Name = _json['Name']
        _Password = _json['Password']
        _Location = _json['Location']
        if _PersonID and _Name and _Password and _Location and request.method == 'POST':
            sql = text("INSERT INTO Person(PersonID, Name, Password, Location) VALUES(:PersonID, :Name, :Password, :Location)")
            data = {"PersonID": _PersonID, "Name": _Name, "Password": _Password, "Location": _Location}
            db.session.execute(sql, data)
            db.session.commit()
            response_object['message'] = 'Person added!'
            return jsonify(response_object)
        else:
            response_object['message'] = 'Invalid data'
            response_object['status'] = 'failed'
            return jsonify(response_object)
    except Exception as e:
        response_object['error'] = str(e)
        response_object['status'] = 'failed'
        app.logger.error(str(e))
        return jsonify(response_object)


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


@app.route('/api/addEvent', methods=['POST'])
def add_event():
    response_object = {'status': 'success'}
    try:
        _json = request.json
        _P1_ID = _json['P1_ID']
        _P2_ID = "00000000"
        _Time = _json['Time']
        _FoodType = _json['FoodType']
        _StationID = _json['StationID']

        if _P1_ID and _Time and _FoodType and _StationID and request.method == 'POST':
            sql = text("INSERT INTO Event(P1_ID, P2_ID, Time, FoodType, StationID) VALUES(:P1_ID, :P2_ID, :Time, :FoodType, :StationID)")
            data = {"P1_ID": _P1_ID, "P2_ID": _P2_ID, "Time": _Time, "FoodType": _FoodType, "StationID": _StationID}
            db.session.execute(sql, data)
            db.session.commit()
            response_object['message'] = 'Event added!'
        else:
            response_object['message'] = 'Invalid data'
            response_object['status'] = 'failed'

    except Exception as e:
        response_object['error'] = str(e)
        response_object['status'] = 'failed'
        app.logger.error(str(e))

    return jsonify(response_object)


@app.route('/api/randomEvent', methods=['GET'])
def random_event():
    p2_ID = request.args.get('p2_ID')
    time_str = request.args.get('time')
    food_type = request.args.get('food_type', 'All')
    station = request.args.get('station', 'All')

    time = datetime.strptime(time_str, '%Y-%m-%d %H:%M:%S')
    time_upper = time + timedelta(hours=1)
    time_lower = time - timedelta(hours=1)

    filters = [
        Event.P2_ID == "00000000",
        Event.Time.between(time_lower, time_upper),
        Event.P1_ID != p2_ID
    ]

    if food_type != 'All':
        filters.append(Event.FoodType == food_type)
    
    if station != 'All':
        filters.append(Event.StationID == station)

    result = Event.query.filter(and_(*filters)).all()

    if result:
        random_event = random.choice(result)
        random_event.P2_ID = p2_ID
        db.session.commit()
        return jsonify({
            'EventID': random_event.EventID,
            'P1_ID': random_event.P1_ID,
            'P2_ID': random_event.P2_ID,
            'Time': random_event.Time,
            'FoodType': random_event.FoodType,
            'StationID': random_event.StationID
        })

    return 'No suitable event found', 404

@app.route('/api/favorite/<person_id>', methods=['GET'])
def get_favorite(person_id):
    favorite_list = db.session.query(FavoriteList).filter_by(PersonID=person_id).all()
    
    if not favorite_list:
        return 'No favorite list found', 404
    
    favorites = []
    for favorite in favorite_list:
        store = db.session.query(Store).get(favorite.StoreID)
        if store is not None:
            favorites.append({'StoreID': store.StoreID, 'Name': store.Name, 'Location': store.Location, 'Distance': store.Distance})
    
    return jsonify(favorites)



if __name__ == '__main__':
    app.run(port=5000)
