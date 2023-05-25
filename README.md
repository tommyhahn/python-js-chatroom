# Chat-Room-App

## Setup and Instructions

Make sure you have python 3.6+ installed.

```bash
pip3 install -r requirements.txt
```

### Running the Server

```bash
cd chatroom
python3 main.py
```
Now we can go to http://localhost:8000/ and start chatting!

### Clearing Message History

To clear the message history simply delete the `messages.db` file.

## Technical overview of the features implemented
Here I am using the builtin Flask-SocketIO to handle bi-directional communications between the clients and the server for this
real-time chatroom without creating a socket on my own and handling servers separately. I am also using Javascript 
for the client-side and sqlite3 as db and storing data in the local messages.db file.

### Features implemented:
1. Users should be able to login and join a singular chatroom via a web client which will bring them to a messenger interface.
2. Users can see previous messages sent by other users when logging in, listed with a timestamp and username they chose to login with.
3. Users can also click on History to see chat history (only messages corresponding to the username they choose to login with)
4. Users can send a message, which will then appear on the chatroom for others to see.
4. Profanity filtering using a third-party API PurgoMalum (free)

## Amount of time I worked on the project
~5 hours


