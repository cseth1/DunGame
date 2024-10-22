from flask import Flask, send_file, request
import game  # Assuming game.py contains the game logic

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def index():
    return send_file('index.html')

# Route to handle commands from the HTML interface
@app.route('/run', methods=['POST'])
def run_command():
    data = request.get_json()
    command = data.get('command')

    # Handle the game commands by using functions from game.py
    if command == "start":
        response = "Game started! Welcome to the adventure."
    else:
        # This assumes that game.py has a function called 'process_command'
        # which takes the command and returns an appropriate response.
        try:
            response = game.process_command(command)
        except AttributeError:
            response = f"Unknown command: {command}"

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
