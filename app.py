# coding: utf-8

from flask import Flask, Response, request, make_response, jsonify
import conn_db
import json
import ast
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World!"

@app.route("/pi",methods=['POST'])
def pi():
	sensor_data = json.loads(request.data)
	print "%f" %sensor_data["sensor"] 
	# if文　送られてきた値が検知範囲外なら値を０に
	if sensor_data["sensor"] < 0.7  or  sensor_data["sensor"] >= 4:
		sensor_data["sensor"] = 0
	insert_db = conn_db.Conn_db()
	insert_db.insertData(sensor_data["sensor"],datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
	return "%f" %sensor_data["sensor"]

@app.route("/get",methods=['GET'])
def get():
	distance_db = conn_db.Conn_db()
	distance, time = distance_db.selectNewDistance()
	response = jsonify({'distance':distance,'time':time})
	response.status_code=200
	return response #float object is not callebled

@app.route("/post",methods=['POST'])
def post():
	#辞書風文字列を辞書型配列に変換
	data = ast.literal_eval(request.data) 
	print request.headers
	print "body: %s\n" % request.data
	#コンストラクタはUUID、Major、Minorを入れる
	beacon_name = conn_db.Conn_db(data["uuid"],data["major"],data["minor"])
	response = make_response(beacon_name.getBeaconName())
	response.headers["Content-Type"] = "text/plain; charset=utf-8"
	print response.data
	return response

if __name__ == "__main__":
	app.run(host = "133.2.113.168",port = 80)
