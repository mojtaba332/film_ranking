# importeer de benodigde packages
import sqlite3
from os import mkdir
from flask import Flask, jsonify
from flask_cors import CORS

DB_FOLDER = 'data'
DB_LOCATION = DB_FOLDER + '/films.db'

app = Flask(__name__)

def get_conn() -> sqlite3.connect:
    # Maak verbinding met de SQLite-database
    try:
        conn = sqlite3.connect(DB_LOCATION, check_same_thread=False)
    except sqlite3.OperationalError:
        mkdir(DB_FOLDER)
    finally:
        conn = sqlite3.connect(DB_LOCATION, check_same_thread=False)
    return conn

def close_conn(connection):
# Maak verbinding met de SQLite-database
    connection.close() 


@app.route('/init', methods=["GET"])
def init_db():
    conn = get_conn()
    c = conn.cursor()
    # Maak de tabel 'films' aan als deze nog niet bestaat
    c.execute('''
        CREATE TABLE IF NOT EXISTS films (
            id INTEGER PRIMARY KEY,
            title TEXT,
            rank INTEGER
        )
    ''')

    # Voeg wat voorbeeldfilms toe aan de database
    c.execute("INSERT INTO films (title, rank) VALUES ('The Shawshank Redemption', 9.3)")
    c.execute("INSERT INTO films (title, rank) VALUES ('The Godfather', 9.2)")
    c.execute("INSERT INTO films (title, rank) VALUES ('The Godfather: Part II', 9.0)")
    conn.commit()
    close_conn(conn)
    return jsonify({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/films', methods=["GET"])
def get_films():
    conn = get_conn()
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    # Haal de lijst met films op uit de database
    c.execute('SELECT * FROM films')
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