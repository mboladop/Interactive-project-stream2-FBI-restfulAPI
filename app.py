import os
import requests
from flask import Flask, jsonify
from flask_cors import cross_origin
import json


app = Flask(__name__)

@app.route("/offenders/<crime>")
@cross_origin() # allow all origins all methods.
def offenders(crime):
    r = requests.get('https://api.usa.gov/crime/fbi/sapi/api/nibrs/'+crime+'/offender/national/race?api_key='+ os.getenv('API_KEY'), verify=False).json()
    return jsonify(r)

@app.route("/victims/<crime>")
@cross_origin() # allow all origins all methods.
def victims(crime):
    r = requests.get('https://api.usa.gov/crime/fbi/sapi/api/nibrs/'+crime+'/victim/national/race?api_key='+ os.getenv('API_KEY'), verify=False).json()
    return jsonify(r)
    
if __name__ == '__main__':
     app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)