from app import create_app, socketio
import os
app = create_app(debug=True)

if os.environ.get('PORT'):
	port = os.environ.get('PORT')
else:
	if os.getenv('PORT'):
		port = getenv('PORT')
	else:
		port = 5000

import sys
print(sys.argv[len(sys.argv)-1])
sys.stdout.flush()

if __name__ == '__main__':
	socketio.run(app, logger=True, engineio_logger=True, port=int(sys.argv[len(sys.argv)-1]))