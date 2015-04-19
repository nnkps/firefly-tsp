#!/usr/bin/python3

from flask import Flask, request, jsonify, send_from_directory
from time import time
import hashlib
import threading
import random

from fireflies import TSPSolver

app = Flask(__name__)

state = {}
STATIC_FOLDER = 'gui-app/build/dist'

@app.route("/run", methods=['POST'])
def run():
    global state

    params = request.get_json()

    while True:
        id = generate_hash()
        if id not in state:
            break

    next_random = lambda: random.random() * 100
    locations = [(next_random(), next_random()) for i in range(params.pop('number_of_cities'))]

    run_in_thread(id, locations, params)

    return jsonify(id=id, route=map_locations_to_json(locations))

@app.route("/state/<string:id>")
def get_state(id):
    global state

    solver, locations = state[id]['solver'], state[id]['locations']
    new_locations = [locations[i] for i in solver.best_solution]

    return jsonify(route=map_locations_to_json(new_locations))

@app.route('/')
def root():
    return send_from_directory(STATIC_FOLDER, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(STATIC_FOLDER, path)

def generate_hash():
    return hashlib.md5(str(time())).hexdigest()

def run_in_thread(key, locations, params):
    def target(key, locations, params):
        global state
        state[key] = {
            'solver': TSPSolver(locations),
            'locations': locations
        }
        state[key]['solver'].run(**params)

    t = threading.Thread(target=target, args=(key, locations, params))
    t.start()

def map_locations_to_json(locations):
    return map(lambda i: { 'x': i[0], 'y': i[1] }, locations)

if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0', port=80)
