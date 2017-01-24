# coding: UTF-8
import sys
import mysql.connector

class Show_db(object):

	def __init__(self):
		self.first_data = None
		self.second_data = None
		self.i = 0

	def setNew(self,first_data):
		self.first_data = first_data

	def setSecond(self,second_data):
		self.second_data = second_data

if __name__ == "__main__":
	show = Show_db()
	connect = mysql.connector.connect(db="test",
					  host="localhost",
					  port="3306",
					  user="test_user",
					  passwd="test3823",
					  charset="utf8")
	cur = connect.cursor()
	select_SQL = "SELECT distance, time FROM sensor ORDER BY time DESC LIMIT 2"
	cur.execute(select_SQL)
	rows = cur.fetchall()
	
	for row in rows:
		if show.i == 0:
			show.setNew(row)
		show.setSecond(row)
		show.i += 1
		
	cur.close()
	connect.close()
	
	print show.first_data
	print show.second_data
	if show.first_data[1] == show.first_data[1]:
		print "true" 	
