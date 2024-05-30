from flask import Blueprint, request, jsonify
from models import Television, Microwave, PumpingMachine, LightBulb, ElectricCooker, db

appliance = Blueprint('appliance', __name__)

@appliance.route('/<appliance>', methods=['GET', 'POST'])
def handle_appliance(appliance):
    if appliance == 'television':
        appliance_instance = Television.query.first()
    elif appliance == 'microwave':
        appliance_instance = Microwave.query.first()
    elif appliance == 'pumping_machine':
        appliance_instance = PumpingMachine.query.first()
    elif appliance == 'light_bulb':
        appliance_instance = LightBulb.query.first()
    elif appliance == 'electric_cooker':
        appliance_instance = ElectricCooker.query.first()
    else:
        return jsonify({'error': 'Invalid appliance type'}), 400

    if request.method == 'POST':
        data = request.json
        appliance_instance.state = data['state']
        db.session.commit()
        uccess = send_state_to_remote(data['state'], appliance)
        return jsonify({'message': f'{appliance} state updated to {data["state"]}'})

    return jsonify({'state': appliance_instance.state})

