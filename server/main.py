# importeer de benodigde packages
# voor nu zijn er een 3-tal werkende request: 
# http://127.0.0.1:5000 - tekst: De server draait in ieder geval naar behoren!
# http://127.0.0.1:5000/init - creeer en vul db
# http://127.0.0.1:5000/films - geft een lijst films
# http://127.0.0.1:5000/film/1 - geeft de film met id 1


from flask import Flask, request
from flask_cors import CORS
from db_actions import *

app = Flask(__name__)

@app.route('/init', methods=["GET"])
def init_db():
    return init_database()

@app.route('/films', methods=["GET"])
def get_films():
    return get_all_films()

@app.route('/films/ranking/<limit>', methods=["GET"])
def get_ranking(limit):
    return get_films_ranking(limit)

@app.route('/film/<film_id>', methods=["GET"])
def get_film(film_id):
    return get_one_film(film_id)

@app.route('/film/delete/<film_id>', methods=["DELETE"])
def delete_film(film_id):
    return delete_one_film(film_id)

@app.route('/film/create', methods=["PUT"])
def create_film():
    # get data from post request
    data = request.get_json(force=True)
    try:
        resp = insert_film(data)
    except ValueError as e:
        resp = jsonify(str(e))
        resp.status_code = 400

    # en geef response terug
    return resp

@app.route('/ranking/rank', methods=["PUT"])
def ranking_rank_film():
    # get data from post request
    data = request.get_json(force=True)
    try:
        resp = rank_film(data)
    except ValueError as e:
        resp = jsonify(str(e))
        resp.status_code = 400

    # en geef response terug
    return resp

@app.route('/user/create', methods=["PUT"])
def create_user():
    # get data from post request
    data = request.get_json(force=True)
    try:
        resp = insert_ranking_user(data)
    except ValueError as e:
        resp = jsonify(str(e))
        resp.status_code = 400

    # en geef response terug
    return resp


@app.route('/', methods=["GET"])
def index():
    return 'De server draait in ieder geval naar behoren!'


CORS(app)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)