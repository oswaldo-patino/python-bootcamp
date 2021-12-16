from flask import Flask, request, jsonify
import requests

from . import app

@app.route("/api/todos")
def todo():
    """
    """
    # Get the json from TODOS
    response = requests.get("http://jsonplaceholder.typicode.com/todos/")
    json = response.json()
    # Get completed and name params
    completed = request.args.get("completed", type=lambda x: x.lower() == 'true', default=True)
    name = request.args.get("name")
    userId = request.args.get("userId", type=int, default = 0)
    # Filter by completed
    json = [x for x in json if x["completed"] == completed]
    # Filter by name
    if name is not None:
        json = [x for x in json if name in x["title"]]
    # Filter by userId
    if userId != 0:
        json = [x for x in json if x["userId"] == userId]
    
    return jsonify(json)