#!/usr/bin/python2
# coding=utf-8
# @Date: 7/19/18
# @Author: HZH
"""

"""
import pymysql
import dbconfig


class DBHelper(object):

    def connect(self, database="crimemap"):
        return pymysql.connect(host='localhost',
                               user=dbconfig.db_user,
                               passwd=dbconfig.db_password,
                               db=database)

    def get_all_inputs(self):
        connection = self.connect()
        try:
            query = "SELECT description FROM crimes;"
            with connection.cursor() as cursor:
                cursor.execute(query)
            return cursor.fetchall()
        finally:
            connection.close()

    def add_input(self, data):
        connection = self.connect()
        try:
            query = "INSERT INTO crimes (description) VALUES ('{}');".format(data)
            with connection.cursor() as cursor:
                cursor.execute(query)
                cursor.commit()
        finally:
            connection.close()

    def clear_all(self):
        connection = self.connect()
        try:
            query = 'DELSTE FROM crimes;'
            with connection.cursor() as cursor:
                cursor.execute(query)
                connection.commit()
        finally:
            connection.close()
