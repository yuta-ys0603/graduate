# coding: UTF-8
import sys
import mysql.connector
import json
from datetime import datetime

class Conn_db(object):
	def __init__(self,uuid="",major=0,minor=0):
		self.uuid = uuid
		self.major = major
		self.minor = minor
		self.result = None

	def getBeaconName(self):
		connect = mysql.connector.connect(db="test",
						 host="localhost",
						 port=3306,
						 user="test_user",
						 passwd="test3823",
						 charset="utf8")

		cur=connect.cursor()
		select_SQL = "SELECT * FROM beacons WHERE uuid = '%s'" % self.uuid + "AND major = '%d'" % self.major + "AND minor = '%d'" % self.minor
		cur.execute(select_SQL)
		rows = cur.fetchall()
		for row in rows:
			self.result = row[1]
		cur.close()
		connect.close()
		print "SELECT SUCCESS"
		return self.result

	def insertData(self,distance,data_time):
		connect = mysql.connector.connect(db="test",
                                                 host="localhost",
                                                 port=3306,
                                                 user="test_user",
                                                 passwd="test3823",
                                                 charset="utf8")
		cur = connect.cursor()
		insert_SQL = "INSERT INTO sensor (distance, time) VALUES ('%f'" % distance + ", '%s'" % data_time + ")"
		cur.execute(insert_SQL)
		cur.close()
		connect.close()
		print "INSERT SUCCESS"

	def selectNewDistance(self):
                connect = mysql.connector.connect(db="test",
                                                 host="localhost",
                                                 port=3306,
                                                 user="test_user",
                                                 passwd="test3823",
                                                 charset="utf8")
		cur = connect.cursor()
		select_SQL = "SELECT distance FROM sensor order by time desc limit 1"
		cur.execute(select_SQL)
		rows = cur.fetchall()
		for row in rows:
			self.result = row[0]
		cur.close()
		connect.close()
		return self.result
