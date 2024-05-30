from flask import Flask
from models import db, initialize_appliances
from routes import appliance

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appliances.db'
db.init_app(app)

@app.before_first_request
def setup():
    db.create_all()
    initialize_appliances()

app.register_blueprint(appliance)

if __name__ == '__main__':
    app.run(debug=True)

