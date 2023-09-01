# deze functies geven een sql string terug.

# functie: query alle films
def get_all_films():
    return f"select * from films"

# functie: query 1 film o.b.v. id
def get_one_film(id):
    return f"select * from films where id = {id}"

# verder uit te breiden
