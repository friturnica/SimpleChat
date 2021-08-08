from app import create_app, socketio

app = create_app(debug=True)

if os.environ.get('PORT'):
	port = os.environ.get('PORT')
else:
	port = 5000

if __name__ == '__main__':
	socketio.run(app, port=port)