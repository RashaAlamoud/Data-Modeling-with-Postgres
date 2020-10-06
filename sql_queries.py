# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
(songplay_id serial, 
start_time timestamp, 
user_id varchar NOT NULL, 
level varchar, 
song_id varchar NOT NULL, 
artist_id text, 
session_id int NOT NULL, 
location varchar, 
user_agent text,
PRIMARY KEY(songplay_id))""")


user_table_create = ("""CREATE TABLE IF NOT EXISTS user
(user_id text NOT NULL ,
first_name varchar ,
last_name varchar ,
gender text ,
level varchar,
PRIMARY KEY(user_id))""")


song_table_create = ("""CREATE TABLE IF NOT EXISTS song
(song_id text NOT NULL ,
title varchar ,
artist_id text NOT NULL ,
year int ,
duration float,
PRIMARY KEY(song_id))""")


artist_table_create = ("""CREATE TABLE IF NOT EXISTS artist
(artist_id text NOT NULL ,
name varchar ,
location varchar ,
latitude numeric, 
longitude numeric,
PRIMARY KEY(artist_id))""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time 
(start_time timestamp NOT NULL ,
hour int ,
day int ,week int,
month int,
year int , 
weekday text, 
PRIMARY KEY(start_time))""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplay(songplay_id  , start_time , user_id , level , song_id , artist_id , session_id , location , user_agent )VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""INSERT INTO user (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)ON CONFLICT (user_id) DO UPDATE SET first_name=user.first_name,last_name=user.last_name,gender=user.gender,level=user.level
""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO UPDATE SET title=songs.title,artist_id=songs.artist_id,year=songs.year,duration=songs.duration
""")



artist_table_insert = ("""INSERT INTO artist(artist_id,name,location,latitude,longitude) VALUES (%s, %s, %s, %s, %s)ON CONFLICT (artist_id) DO UPDATE SET name=artist.name,location=artist.location,latitude=artist.latitude,longitude=artist.longitude

""")


time_table_insert = ("""INSERT INTO time(start_time,hour,day,weekofyear,month,year,weekday) VALUES (%s, %s, %s, %s, %s,%s,%s)ON CONFLICT (start_time) DO UPDATE SET hour=time.hour,day=time.day,weekofyear=time.weekofyear,month=time.month,year=time.year,
weekday=time.weekday

""")

# FIND SONGS

song_select = ("""SELECT song.song_id,artist.artist_id FROM song JOIN artist ON song.artist_id = artist.artist_id WHERE song.title=%s AND artist.name=%s AND song.duration =%s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]