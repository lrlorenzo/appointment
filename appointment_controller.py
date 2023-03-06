from flask import Blueprint, Flask, request, jsonify, make_response
from sqlalchemy.exc import NoResultFound

from appointment import Appointment
import appointment_service
from appointment_exception import AppointmentException

app = Flask(__name__)
appointment_controller = Blueprint('appointment_controller', __name__)


@appointment_controller.route('/appointments/', methods=['GET'])
def find_all():
    try:
        appointment = appointment_service.find_all()
        return make_response(jsonify(appointment.to_dict()), 200)
    except AppointmentException as e:
        return make_response(jsonify(str(e)), 500)


@appointment_controller.route('/appointments/<int:appointment_id>', methods=['GET'])
def find_appointment(appointment_id):
    try:
        appointment = appointment_service.find(appointment_id)
        return make_response(jsonify(appointment.to_dict()), 200)
    except NoResultFound as e:
        return make_response(jsonify(str(e)), 404)
    except AppointmentException as e:
        return make_response(jsonify(str(e)), 500)


@appointment_controller.route('/appointments', methods=['POST'])
def add_appointment():
    try:

        appointments = []
        for a in request.json['appointments']:
            print(a)
            resource_id = a['resource_id']
            resource_name = a['resource_name']
            task_id = a['task_id']
            task = a['task']
            start_date = a['start_date']
            end_date = a['end_date']
            status = a['status']
            pct = a['pct']

            appointment = Appointment(resource_id, resource_name, task_id, task, start_date, end_date, status, pct)
            appointments.append(appointment)

        appointment_service.add_appointments(appointments)
        response = {
            'message': 'Appointment Successfully Created',
        }
        return make_response(jsonify(response), 201)

    except:
        error_response = {
            'error': 'Application error occurred',
            'status': 500
        }
        return make_response(jsonify(error_response), 500)
