# DROP TABLES

time_table_drop = "DROP TABLE IF EXISTS songplays;"
songplay_table_drop = "DROP TABLE IF EXISTS time;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"

# CREATE TABLES

artist_table_create = (""" \
CREATE TABLE IF NOT EXISTS artists \
  ( artist_id        varchar \
   ,artist_latitude  real \
   ,artist_longitude real \
   ,artist_location  varchar \
   ,artist_name      varchar \
   ,PRIMARY KEY (artist_id) \
   ,UNIQUE (artist_name) \
  ); \
""")

song_table_create = (""" \
CREATE TABLE IF NOT EXISTS songs \
  ( song_id   varchar \
   ,title     varchar \
   ,duration  real \
   ,year      smallint \
   ,artist_id varchar \
   ,PRIMARY KEY (song_id)
  ); \
""")

user_table_create = (""" \
CREATE TABLE IF NOT EXISTS users \
  ( firstName    varchar \
   ,gender       varchar \
   ,lastName     varchar \
   ,level        varchar \
   ,location     varchar \
   ,userId       int \
   ,PRIMARY KEY (userId) \
  ); \
""")

time_table_create = (""" \
CREATE TABLE IF NOT EXISTS time \
  ( userAgent     varchar \
   ,sessionId     int \
   ,itemInSession int \
   ,timestamp     timestamp \
   ,hour          int \
   ,day           int \
   ,week          int \
   ,month         int \
   ,year          int \
   ,weekday       int \
   ,PRIMARY KEY (sessionId, itemInSession) \
  ); \
""")

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays \
  ( artistId      varchar \
   ,length        real \
   ,songId        varchar \
   ,sessionId     int \
   ,itemInSession int
   ,userId        int \
   ,UNIQUE (artistId, songId, userId, sessionId, itemInSession) \
   ); \
""")

# INSERT RECORDS

artist_table_insert = ("""
INSERT INTO artists
  ( artist_id \
   ,artist_latitude \
   ,artist_longitude \
   ,artist_location \
   ,artist_name \
  ) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (artist_id) \
DO NOTHING; \
""")

song_table_insert = ("""
INSERT INTO songs
  ( song_id \
   ,title \
   ,duration \
   ,year \
   ,artist_id \
  ) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (song_id) \
DO NOTHING; \
""")

user_table_insert = ("""
INSERT INTO users
  ( userId \
   ,firstName \
   ,lastName \
   ,gender \
   ,level \
   ,location \
  )
VALUES (%s, %s, %s, %s, %s, %s) \
ON CONFLICT (userId) \
DO NOTHING; \
""")

not_used_songplay_table_insert = ("""
INSERT INTO time
  ( auth \
   ,itemInSession \
   ,method \
   ,page \
   ,sessionId \
   ,status \
   ,ts \
   ,userAgent \
   ,userId \
  )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s); \
""")

not_used_time_table_insert = ("""
INSERT INTO songplays
  ( artist \
   ,itemInSession \
   ,length \
   ,sessionId \
   ,song \
  )
VALUES (%s, %s, %s, %s, %s); \
""")

time_table_insert = (""" \
INSERT INTO time \
  ( userAgent \
   ,sessionId \
   ,itemInSession \
   ,timestamp \
   ,hour \
   ,day \
   ,week \
   ,month \
   ,year \
   ,weekday \
  )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) \
ON CONFLICT (sessionId, itemInSession) \
DO NOTHING; \
""")

songplay_table_insert = ("""
INSERT INTO songplays \
  ( artistId \
   ,length \
   ,songId \
   ,sessionId \
   ,itemInSession \
   ,userId \
  )
VALUES (%s, %s, %s, %s, %s, %s) \
ON CONFLICT (artistId, songId, userId, sessionId, itemInSession) \
DO NOTHING; \
""")

# FIND SONGS

song_select = (""" \
SELECT \
    t5.artist_id AS artistid \
   ,t4.duration AS length \
   ,t4.song_id AS songid \
   ,t2.sessionId \
   ,t2.itemInSession \
   ,t3.userId \
FROM songplays t1 \
    INNER JOIN time t2 \
        ON t1.sessionId = t2.sessionId \
       AND t1.itemInsession = t2.itemInSession \
    INNER JOIN users t3 \
        ON t1.userId = t3.userId \
    INNER JOIN songs t4 \
        ON t1.songId = t4.song_id \
    INNER JOIN artists t5 \
        ON t1.artistId = t5.artist_id; \
""")

# QUERY LISTS

create_table_queries = [artist_table_create, song_table_create, user_table_create, time_table_create, songplay_table_create]
drop_table_queries = [songplay_table_drop, time_table_drop, user_table_drop, song_table_drop, artist_table_drop]