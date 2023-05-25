import json

import requests
from flask_socketio import SocketIO
from application import create_app
from application.database import DataBase
import config

# SETUP
app = create_app()
socketio = SocketIO(app)  # For user communication


def check_profanity(message, api_url):
    query_string = {"text": message}

    response = requests.get(api_url, params=query_string)

    if response.status_code == 200:
        response_json = json.loads(response.text)
        result_text = response_json["result"]
        return result_text
    else:
        # Request failed, keep the original message
        return message


@socketio.on('event')
def handle_my_custom_event(json):
    """
    handles profanity filtering and saving messages once received from web server
    and sending the filtered message to other clients
    :param json: json
    :param methods: POST GET
    :return: None
    """

    data = dict(json)
    if "name" in data:
        check_profanity_url = "https://www.purgomalum.com/service/json"
        message = data["message"]
        data["message"] = check_profanity(message, check_profanity_url)

        db = DataBase()
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', data)


# MAINLINE
if __name__ == "__main__":  # start the web server
    socketio.run(app, debug=True, host=str(config.Config.SERVER), port=8000)
