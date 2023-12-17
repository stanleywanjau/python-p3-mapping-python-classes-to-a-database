#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song
# import pytest; pytest.set_trace()



if __name__ == '__main__':
#  with CONN:
    Song.create_table()
    
    
    
    CURSOR.execute("PRAGMA table_info(songs)").fetchall()
    
    
    hello = Song("Hello", "25")
    hello.save()

    despacito = Song("Despacito", "Vida")
    despacito.save()

    hello.id
# => 1
    despacito.id

    CONN.commit()

        # Fetch and print all songs
    songs = CURSOR.execute('SELECT * FROM songs').fetchall()
    print("All Songs:")
    for song in songs:
     print(song)
   
  