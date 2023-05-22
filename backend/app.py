from flask import Flask, request, jsonify
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

password = quote_plus("xX@0180368905")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{password}@localhost/mrt_foodmap'  # 你的資料庫URI
db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'Person'  # 確保table name與你的SQL table相同
    PersonID = db.Column(db.String(50), primary_key=True)
    Name = db.Column(db.String(50), nullable=False)
    Password = db.Column(db.String(12), nullable=False)
    Location = db.Column(db.String(50))


CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/person', methods=['GET'])
def get_persons():
    persons = Person.query.all()
    persons_list = [{'PersonID': person.PersonID, 'Name': person.Name, 'Password': person.Password, 'Location': person.Location} for person in persons]
    return jsonify(persons_list)

@app.route('/api/person/<id>', methods=['GET'])
def get_person(id):
    person = Person.query.get(id)
    if person is None:
        return 'No such person', 404
    person_dict = {'PersonID': person.PersonID, 'Name': person.Name, 'Password': person.Password, 'Location': person.Location}
    return jsonify(person_dict)


if __name__ == '__main__':
    app.run(port=5000)
