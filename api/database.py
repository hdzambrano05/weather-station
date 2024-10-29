'''
Dev: Harold Zambrano
Script description: wheather station
Engine: SQLite
'''

#Import engine database package
import sqlite3

#Create weather-station database conncetion
con = sqlite3.connect('weather_station.db')

#Crate cursor
cur = con.cursor()

#Users model

user_model = ''' 
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY ,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESRAMP DEFAULT (datetime ('now', 'localtime')),
        update_at TIMESRAMP DEFAULT (datetime ('now', 'localtime')),
        deleted_at null
    )
'''

stations_model = '''
    CREATE TABLE IF NOT EXISTS stations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL,
        localation TEXT NOT NULL
        status BOOLEAN DEFAULT true
    )

'''

#Execute query
cur.execute(user_model)

#Close connection


