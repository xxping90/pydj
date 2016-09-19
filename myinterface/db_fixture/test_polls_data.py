__author__ = 'xzz'

import sys,os
# sys.path.append('../db_fixture')
test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
print (test_dir)

sys.path.insert(0,test_dir)

from mysql_setting import MySQLOperating
import datetime


#insert table datas
def inster_data(table,datas):
	db = MySQLOperating()
	db.clear(table)
	for data in datas:
		db.insert(table,data)
	db.close()

#create data
table_poll_question = 'polls_question'
datas_poll_question = [{'id':1,'question_text':'you buy pro6?','pub_date':'2016-07-26 15:21:22'}]
table_poll_choice = "polls_choice"
datas_poll_choice = [{'id':1,'choice_text':'buy','votes':0,'question_id':1,},
					{'id':2,'choice_text':'not buy','votes':0,'question_id':1}]

#init data
def init_data():
	inster_data(table_poll_question,datas_poll_question)
	inster_data(table_poll_choice,datas_poll_choice)

if __name__=='__main__':
	init_data()