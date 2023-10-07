import sqlite3
from os import mkdir
from flask import jsonify
from queries import *

DB_FOLDER = 'data/'
DB_LOCATION = DB_FOLDER + 'films.db'

def get_conn() -> sqlite3.connect:
    # Create connection with SQLite-database
    try:
        conn = sqlite3.connect(DB_LOCATION, check_same_thread=False)
    except sqlite3.OperationalError:
        mkdir(DB_FOLDER)
    finally:
        conn = sqlite3.connect(DB_LOCATION, check_same_thread=False)
    return conn


def close_conn(connection):
    connection.close()

def get_all_films():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Haal de lijst met films op uit de database
    c.execute(query_all_films())
    films = [dict(row) for row in c.fetchall()]
    conn.close()

    # Zet de lijst met films om naar JSON-formaat en geef deze terug als antwoord
    return jsonify(films)

def get_films_ranking(limit):
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Haal de lijst met films op uit de database
    c.execute(query_films_ranked_higher(limit))
    films = [dict(row) for row in c.fetchall()]
    conn.close()

    # Zet de lijst met films om naar JSON-formaat en geef deze terug als antwoord
    return jsonify(films)

def get_one_film(film_id: int):
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Haal 1 film op uit de db
    c.execute(query_one_film(film_id))
    films = [dict(row) for row in c.fetchall()]
    conn.close()

    # Zet de lijst met films om naar JSON-formaat en geef deze terug als antwoord
    return jsonify(films[0])

def delete_one_film(film_id: int):
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Delete 1 film
    c.execute(query_delete_film(film_id))
    conn.commit()
    conn.close()

    # Zet de lijst met films om naar JSON-formaat en geef deze terug als antwoord
    return jsonify({'success':True}), 200, {'ContentType':'application/json'}

def insert_film(data):
    # haal titel en film uit data (json)
    title = data["title"]
    description = data["description"]
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Insert 1 record
    c.execute(query_insert_film(title, description))
    row_id = c.lastrowid
    conn.commit()
    conn.close()
    return jsonify({'id' : row_id}), 201, {'ContentType': 'application/json'}

def insert_ranking_user(data):
    # haal titel en film uit data (json)
    first_name = data["first_name"]
    last_name = data["last_name"]
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Insert 1 record
    c.execute(query_insert_ranking_user(first_name, last_name))
    row_id = c.lastrowid
    conn.commit()
    conn.close()
    return jsonify({'id' : row_id}), 201, {'ContentType': 'application/json'}

def rank_film(data):
    # haal titel en film uit data (json)
    film_id = data["film_id"]
    rank = data["rank"] # normally between 1 and 10
    ranked_by = data["ranked_by"] # id of table ranking_user
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Insert 1 record
    c.execute(query_insert_ranking(film_id, rank, ranked_by))
    row_id = c.lastrowid
    conn.commit()
    conn.close()
    return jsonify({'id' : row_id}), 201, {'ContentType': 'application/json'}

def init_database():
    conn = get_conn()
    c = conn.cursor()

    # remove tables
    c.execute(drop_film())
    c.execute(drop_ranking())
    c.execute(drop_ranked_by())
    c.execute(drop_ranking_users())
    conn.commit()
    # create tables
    c.execute(create_table_film())
    c.execute(create_table_ranking_user())
    c.execute(create_table_ranking())
    # Insert dummy data
    c.execute(get_dummy_films())
    c.execute(get_dummy_ranking_users())
    c.execute(get_dummy_rankings())
    conn.commit()
    close_conn(conn)
    return jsonify({'success': True}), 200, {'ContentType': 'application/json'}
