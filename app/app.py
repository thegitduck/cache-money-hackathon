from helpers import *
from flask import Flask, jsonify, request
import sqlite3 as sql
from geocoder import ip

app = Flask(__name__)
DB = f"{get_proj_dir()}/database.db"

@app.route('/locations', methods=['GET', 'POST'])
def get_locations():
	if request.method == 'GET':
	  with sql.connect(DB) as conn:
	  	return jsonify(dict(results=[tuple(row) for row in conn.execute("SELECT * FROM Trucks").fetchall()]))

	elif request.method == 'POST':
		with sql.connect(DB) as conn:
			req_data = request.get_json(force=True)
			coordinates = ip('me').latlng
			try:
				conn.execute(f"INSERT INTO Trucks (Name, Latitude, Longitude) VALUES ('{req_data['name']}', {coordinates[0]}, {coordinates[1]});")
			except sql.IntegrityError:
				return "failure Truck already exists"
			return "success"		
