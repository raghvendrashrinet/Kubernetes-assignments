from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store for todos
# Note: Because this is in-memory, restarting the container resets the list.
todos = [
    "Learn JavaScript",
    "Learn React",
    "Build a project"
]

@app.route('/todos', methods=['GET'])
def get_todos():
    """Returns the current list of todos as JSON."""
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    """Appends a new todo item sent from the frontend."""
    # Read incoming data safely from either JSON payload or standard Form post
    data = request.get_json() or request.form
    
    new_todo = data.get("content")
    if new_todo:
        todos.append(new_todo)
        
    return jsonify(todos), 201

if __name__ == '__main__':
    # host='0.0.0.0' allows external traffic (like the frontend container) to connect.
    # port=3000 matches your containerPort configuration.
    app.run(host='0.0.0.0', port=3000)
