# File: song.py

import sqlite3

class Song:
    def __init__(self, name, album):
        self.id = None
        self.name = name
        self.album = album

    @staticmethod
    def create_table():
        with sqlite3.connect("music.db") as connection:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS songs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    album TEXT
                )
            ''')

    def save(self):
        with sqlite3.connect("music.db") as connection:
            cursor = connection.cursor()

            
            cursor.execute('''
                INSERT INTO songs (name, album)
                VALUES (?, ?)
            ''', (self.name, self.album))
            self.id = cursor.lastrowid


    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song
