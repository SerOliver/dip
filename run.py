#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask import jsonify
from flask import request
import json

from plot import preporuka

app = Flask(__name__, static_folder='www')

@app.route('/<path:path>')
def static_file(path):
    try:
        return app.send_static_file(path)
    except:
        return "Error"

@app.route('/api/preporuka', methods=['POST'])
def app_preporuka():
    obj = request.json
    #print(obj)
    #print(obj['param1'])
    #print(obj['param2'])
    #print(obj['param3'])
    # ovde ide veliki posao odredjivanja preporuke
    #p = obj('param1')
    ret = preporuka()
    rez = {'x': ret[0]}
    print(rez)
    return jsonify(rez)

#@app.route('/api/filmovi', methods=['GET'])
#def get_films():
# 	search = request.args.get("search")
#    return jsonify(rez)


@app.route('/')
def root():
    return app.send_static_file('index.html')

app.run(host='0.0.0.0', port=8585, debug=True, use_reloader=True)
