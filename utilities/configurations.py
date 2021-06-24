import configparser
import mysql.connector
from mysql.connector import Error


# method to parse config
def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


# create config connection to sql
connect_config = {
    'user': getConfig()['SQL']['sqlUser'],
    'password': getConfig()['SQL']['sqlPassword'],
    'host': getConfig()['SQL']['sqlHost'],
    'database': getConfig()['SQL']['sqlDatabase'],

}


# method to authenticate git login
def auth_gitLogin():
    gitUser = 'vyhoang'
    gitToken = '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'
    return gitUser, gitToken


# method to connect sql database
def getSQLConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection successful")
            return conn
    except Error as e:
        print(e)


# method to execute query and get first row from db
def getQuery(query):
    conn = getSQLConnection()
    cursorObj = conn.cursor()
    cursorObj.execute(query)
    row = cursorObj.fetchone()
    conn.close()
    return row
