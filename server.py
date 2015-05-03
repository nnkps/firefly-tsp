#!/usr/bin/python3

from flask import Flask, request, jsonify, send_from_directory
from time import time
import hashlib
import threading
import random
from City import *

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

    # next_random = lambda: random.random() * 100
    # locations = [(next_random(), next_random()) for i in range(]
    cities = [(37, 52), (49, 49), (52, 64), (20, 26), (40, 30), (21, 47), (17, 63), (31, 62), (52, 33), (51, 21), (42, 41), (31, 32), (5, 25), (12, 42), (36, 16), (52, 41), (27, 23), (17, 33), (13, 13), (57, 58), (62, 42), (42, 57), (16, 57), (8, 52), (7, 38), (27, 68), (30, 48), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (46, 10), (61, 33), (62, 63), (63, 69), (32, 22), (45, 35), (59, 15), (5, 6), (10, 17), (21, 10), (5, 64), (30, 15), (39, 10), (32, 39), (25, 32), (25, 55), (48, 28), (56, 37), (30, 40)]
    locations = [City(element[0], element[1]) for element in cities]
    params.pop('number_of_cities')

    run_in_thread(id, locations, params)

    return jsonify(id=id, route=map_locations_to_json(locations))

@app.route("/state/<string:id>")
def get_state(id):
    global state

    solver, locations, done = state[id]['solver'], state[id]['locations'], state[id]['done']
    new_locations = [locations[i] for i in solver.best_solution]

    return jsonify(route=map_locations_to_json(new_locations), done=done)

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
            'locations': locations,
            'done': False
        }
        state[key]['solver'].run(**params)
        state[key]['done'] = True

    t = threading.Thread(target=target, args=(key, locations, params))
    t.start()

def map_locations_to_json(locations):
    return map(lambda i: { 'x': i.x, 'y': i.y }, locations)

if __name__ == "__main__":
    # app.debug = True
    app.run(host='0.0.0.0', port=80)
