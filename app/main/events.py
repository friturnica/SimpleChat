from flask import session, redirect, url_for
from flask_socketio import emit, join_room, leave_room
from .. import socketio

clients = {}

@socketio.on('joined', namespace='/chat')
def joined(message):
	"""Sent by clients when they enter a room.
	A status message is broadcast to all people in the room."""
	room = session.get('room')
	if not(room in clients):
		clients[room] = []
	if session.get('name') in clients[room]:
		return emit('redirect', {'url': url_for('main.index'), 'msg': 'пользователь с таким никнеймом уже в чате!'})

	clients[room].append(session.get('name'))
	join_room(room)
	emit('status', {'msg': session.get('name') + ' зашёл в комнату!', 'clients': clients[room]}, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
	"""Sent by a client when the user entered a new message.
	The message is sent to all people in the room."""
	if message['msg'].strip() == "" or len(message['msg'])>96:
		return
	room = session.get('room')
	emit('message', {'msg': session.get('name') + ': ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
	"""Sent by clients when they leave a room.
	A status message is broadcast to all people in the room."""
	room = session.get('room')
	clients[room].remove(session.get('name'))
	leave_room(room)
	emit('status', {'msg': session.get('name') + ' вышел из комнаты!', 'clients': clients[room]}, room=room)

