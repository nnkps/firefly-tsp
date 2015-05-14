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

@app.route('/')
def root():
    return send_from_directory(STATIC_FOLDER, 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(STATIC_FOLDER, path)

@app.route("/run", methods=['POST'])
def run():
    global state

    params = request.get_json()

    while True:
        id = generate_hash()
        if id not in state:
            break

    tsplib_data = params.pop('tsplib_data')
    locations = parse_tsplib_data(tsplib_data)

    heuristics = params.pop('heurestics')
    params['heuristics_percents'] = (heuristics['nearest_neighbour'], heuristics['nearest_insertion'], heuristics['random'])

    run_in_thread(id, locations, params)

    return jsonify(id=id, route=map_locations_to_json(locations))

@app.route("/state/<string:id>")
def get_state(id):
    global state

    solver, locations, done = state[id]['solver'], state[id]['locations'], state[id]['done']
    new_locations = [locations[i] for i in solver.best_solution]
    route_cost = solver.best_solution_cost

    return jsonify(route=map_locations_to_json(new_locations), route_cost=route_cost, done=done, iteration=solver.n)

def generate_hash():
    return hashlib.md5(str(time()).encode('utf-8')).hexdigest()

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

def parse_tsplib_data(data):
    def parse_line(line):
        line_split = line.split()
        return City(float(line_split[1]), float(line_split[2]))

    lines = data.strip().split('\n')[6:-1]
    return map(parse_line, lines)

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=80)
