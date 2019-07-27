from helpers import *
from json import loads
from flask import Flask, jsonify, request
import sqlite3 as sql
from geocoder import ip
from flask_cors import CORS

app = Flask(__name__)
DB = f"{get_proj_dir()}/database.db"

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
CORS(app)


@app.route('/locations', methods=['GET', 'POST'])
def get_locations():
	if request.method == 'GET':
	  with sql.connect(DB) as conn:
	  	return jsonify(dict(results=[tuple(row) for row in conn.execute("SELECT Name, Latitude, Longitude FROM Trucks").fetchall()]))

	elif request.method == 'POST':
		with sql.connect(DB) as conn:
			req_data = request.get_json(force=True)
			try:
				conn.execute(f"INSERT INTO Trucks (Name, Latitude, Longitude) VALUES (\"{req_data['name']}\", {req_data['latitude']}, {req_data['longitude']});")
			except sql.IntegrityError:
				return "Failure: Truck already exists"
			return "success"		

app.run()