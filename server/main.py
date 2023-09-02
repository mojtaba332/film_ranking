# importeer de benodigde packages
# voor nu zijn er een 3-tal werkende request: 
# http://127.0.0.1:5000 - tekst: De server draait in ieder geval naar behoren!
# http://127.0.0.1:5000/init - creeer en vul db
# http://127.0.0.1:5000/films - geft een lijst fims


import sqlite3
from os import mkdir
from flask import Flask, jsonify
from flask_cors import CORS
from queries import *

DB_FOLDER = 'data/'
DB_LOCATION = DB_FOLDER + 'films.db'

app = Flask(__name__)

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

@app.route('/init', methods=["GET"])
def init_db():
    conn = get_conn()
    c = conn.cursor()

    # remove tables
    c.execute(drop_film())
    c.execute(drop_ranking())
    c.execute(drop_ranked_by())
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
    return jsonify({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/films', methods=["GET"])
def get_films():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Haal de lijst met films op uit de database
    c.execute(get_all_films())
    films = [dict(row) for row in c.fetchall()]
    conn.close()

    # Zet de lijst met films om naar JSON-formaat en geef deze terug als antwoord
    return jsonify(films)

@app.route('/', methods=["GET"])
def index():
    return 'De server draait in ieder geval naar behoren!'


CORS(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)