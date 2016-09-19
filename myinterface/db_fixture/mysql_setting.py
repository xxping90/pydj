__author__ = 'xzz'

import pymysql.cursors
import datetime

#==========Setting linked test databases ================
host = "127.0.0.1"
user = 'root'
password = 'qwe123'
db = 'polls'

#========MySql base operating ================
class MySQLOperating():
	def __init__(self):
		try:
			#Connect to the database
			self.connection = pymysql.connect(host = host,
												user = user,
												password =password,
												db=db,
												charset='utf8mb4',
												cursorclass=pymysql.cursors.DictCursor
												)
		except pymysql.err.OperationalError as e:
			print("Mysql Error %d:%s" % (e.args[0],e.args[1]))

	#clear table data
	def clear(self,table_name):
		real_sql = "delete from " + table_name + ";"
		with self.connection.cursor() as cursor:
			cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
			cursor.execute(real_sql)
		self.connection.commit()

	#insert sql statment
	def insert(self,table_name,data):
		for key in data:
			data[key] = "'" + str(data[key]) + "'"
		key = ','.join(data.keys())
		value = ','.join(data.values())
		real_sql = "INSERT INTO " + table_name + "(" + key + ") VALUES (" + value +")"

		print (real_sql)

		with self.connection.cursor() as cursor:
			cursor.execute(real_sql)
		self.connection.commit()

	#close database
	def close(self):
		self.connection.close()

if __name__ == '__main__':
	db = MySQLOperating()
	date =datetime.datetime.now()
	print (date)

	table_name ='polls_question'
	data = {'id':1,'question_text':'you buy pro6?','pub_date':date}

	db.clear(table_name)
	db.insert(table_name,data)
	db.close()
