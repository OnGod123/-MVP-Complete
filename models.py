from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appliances.db'
db = SQLAlchemy(app)

db = SQLAlchemy()

class Television(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default=False)

class Microwave(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default=False)

class PumpingMachine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default=False)

class LightBulb(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default=False)

class ElectricCooker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.Boolean, default=False)

def initialize_appliances():
    if Television.query.first() is None:
        db.session.add(Television(state=False))
    if Microwave.query.first() is None:
        db.session.add(Microwave(state=False))
    if PumpingMachine.query.first() is None:
        db.session.add(PumpingMachine(state=False))
    if LightBulb.query.first() is None:
        db.session.add(LightBulb(state=False))
    if ElectricCooker.query.first() is None:
        db.session.add(ElectricCooker(state=False))
    db.session.commit()

