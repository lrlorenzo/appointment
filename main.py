from flask import Flask, jsonify
from appointment_controller import appointment_controller

app = Flask(__name__)
app.register_blueprint(appointment_controller, url_prefix='/appointment_api')

if __name__ == '__main__':
    app.run(port=5003, debug=True)

