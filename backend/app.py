from flask import Flask, request, jsonify
from urllib.parse import quote_plus
# from flask_sqlalchemy import SQLAlchemy,text, or_, and_
from sqlalchemy.sql.expression import between
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, or_, and_

import random
from datetime import datetime, timedelta


password = quote_plus("xX@0180368905")
# password = quote_plus("00000")
# password = quote_plus("221003red")

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/mrt_foodmap'  # 你的資料庫URI
app.config['DEBUG'] = True
db = SQLAlchemy(app)

@app.errorhandler(500)
def handle_500(error):
    app.logger.error(f"500 error: {error}")  # Log the error
    return jsonify({"status": "failed", "message": "Internal server error"}), 500

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

    def __init__(self, PersonID, StoreID):
        self.PersonID = PersonID
        self.StoreID = StoreID

class HistoryList(db.Model):
    __tablename__ = 'HistoryList'
    HListID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    PersonID = db.Column(db.String(50), nullable=False)
    StoreID = db.Column(db.String(50), nullable=False)

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
        _P2_ID = "0"
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


@app.route('/api/randomPair', methods=['POST'])
def pair_event():
    try:
        data = request.get_json()
        data['Time'] = datetime.strptime(data['Time'], '%Y-%m-%d %H:%M:%S')

        query = text("""
            SELECT EventID, P1_ID, P2_ID, Time, FoodType, StationID FROM Event
            WHERE P2_ID = "0"
            AND ABS(TIMESTAMPDIFF(MINUTE, Time, :Time)) <= 60
            AND FoodType = :FoodType
            AND StationID = :StationID
            ORDER BY RAND()
            LIMIT 1
        """)

        # Execute the query
        result = db.session.execute(query, data).fetchone()
        result_dict = dict(result._asdict())  # Convert the result tuple to a dictionary
        # print(data)
        

        if result:
            # Change the P2_ID of the selected event to the passed P2_ID
            update_query = text("""
                UPDATE Event SET P2_ID = :P2_ID WHERE EventID = :id
            """)
            db.session.execute(update_query, {"P2_ID": data['P2_ID'], "id": result_dict['EventID']})
            
            db.session.commit()
            return jsonify({"status": "success", "event": result_dict}), 200
        else:
            return jsonify({"status": "failed", "message": "No available pair"}), 404

    except Exception as e:
        app.logger.error(str(e))
        return jsonify({"status": "failed", "message": str(e)}), 500

@app.route('/api/favorite/<person_id>', methods=['GET'])
def get_favorite(person_id):
    favorite_list = db.session.query(FavoriteList).filter_by(PersonID=person_id).all()
    
    if not favorite_list:
        return 'No favorite list found', 404
    
    favorites = []
    for favorite in favorite_list:
        store = db.session.query(Store).get(favorite.StoreID)
        if store is not None:
            favorites.append({'FListID': favorite.FListID, 'StoreID': store.StoreID, 'Name': store.Name, 'Location': store.Location, 'Distance': store.Distance})
    
    return jsonify(favorites)

@app.route('/api/history/<person_id>', methods=['GET'])
def get_history(person_id):
    history_list = db.session.query(HistoryList).filter_by(PersonID=person_id).all()
    
    if not history_list:
        return 'No favorite list found', 404
    
    histories = []
    for history in history_list:
        store = db.session.query(Store).get(history.StoreID)
        if store is not None:
            histories.append({'HListID': history.HListID, 'StoreID': store.StoreID, 'Name': store.Name, 'Location': store.Location, 'Distance': store.Distance})
    
    return jsonify(histories)


if __name__ == '__main__':
    app.run(port=5000)
