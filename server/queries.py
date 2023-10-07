# deze functies geven een sql string terug.

# functie: query alle films
def query_all_films():
    return "select * from film;"

# functie: query films met een rang hoger dan rank
def query_films_ranked_higher(limit):
    return f"select film.id as id, film.title as title, (select round(max(rank),1) from ranking where ranking.film_id = film.id) as rank from film order by rank asc limit 3;"

# functie: query 1 film o.b.v. id
def query_one_film(id):
    return f"select * from film where id = {id};"

def query_delete_film(id):
    return f"delete from film where id = {id}"

def query_insert_film(title, description):
    return f'''insert into film (title, description) 
                VALUES ("{title}", "{description}")'''

def query_insert_ranking_user(first_name, last_name):
    return f'''insert into ranking_user (first_name, last_name) 
                VALUES ("{first_name}", "{last_name}")'''

def query_insert_ranking(film_id, rank, ranked_by):
    return f'''insert into ranking (film_id, rank, ranked_by) 
                VALUES ("{film_id}", "{rank}", "{ranked_by}")'''

# From here on you find the inserts, creates and delete etc.
# Please do not change

def drop_film():
    return 'DROP TABLE IF EXISTS film;'

def drop_ranking():
    return 'DROP TABLE IF EXISTS ranking'

def drop_ranked_by():
    return 'DROP TABLE IF EXISTS ranked_by'

def drop_ranking_users():
    return 'DROP TABLE IF EXISTS ranking_user'

def create_table_film():
    return '''
        CREATE TABLE IF NOT EXISTS film (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR(50),
            description TEXT
        );
    '''

def create_table_ranking():
    return '''
        CREATE TABLE IF NOT EXISTS ranking (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            film_id INTEGER,
            rank NUMERIC,
            ranked_by INTEGER,
            FOREIGN KEY (film_id) REFERENCES film (id),            
            FOREIGN KEY (ranked_by) REFERENCES ranking_user (id)
        ) ;
        '''

def create_table_ranking_user():
    return '''
        CREATE TABLE IF NOT EXISTS ranking_user (
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             first_name varchar(50),                             
             last_name varchar(50)                
        );
    '''

def get_dummy_films():
    return '''
       INSERT INTO film (id, title, description)
        VALUES 
        (1, 'The Lion King', 'Disney animated film about a lion cub named Simba.'),
        (2, 'Frozen', 'Disney animated film about two sisters, Elsa and Anna.'),
        (3, 'Toy Story', 'Disney animated film about the adventures of a group of toys.'),
        (4, 'Skyfall', 'James Bond film starring Daniel Craig as 007.'),
        (5, 'Barbie in the Nutcracker', 'Animated film featuring Barbie as Clara in the Nutcracker story.'),
        (6, 'The Shawshank Redemption', 'Drama film about a man wrongfully convicted of murder.');               
           '''

def get_dummy_ranking_users():
    return '''
        INSERT INTO ranking_user (id, first_name, last_name)
        VALUES 
        (1, 'Jan', 'de Tester'),
        (2, 'Fatima', 'Ahmed'),
        (3, 'Chen', 'Wang'),
        (4, 'Sofia', 'Garcia'),
        (5, 'Lucas', 'Silva'),
        (6, 'Emmanuel', 'Koffi'),
        (7, 'Nina', 'Ivanova'),
        (8, 'Oliver', 'Nielsen'),
        (9, 'Yasmin', 'Al-Hassan'),
        (10, 'Kenji', 'Sato');
    '''

def get_dummy_rankings():
    return '''
    INSERT INTO ranking (film_id, rank, ranked_by) 
    VALUES
    (1, 9.5, 1),
    (2, 8.3, 2),
    (3, 7.2, 3),
    (4, 6.4, 4),
    (5, 5.6, 5),
    (6, 4.8, 6),
    (1, 3.9, 7),
    (2, 3.1, 8),
    (3, 2.3, 9),
    (4, 1.5, 10),
    (5, 9.4, 1),
    (6, 8.6, 2),
    (1, 7.8, 3),
    (2, 7.0, 4),
    (3, 6.2, 5),
    (4, 5.4, 6),
    (5, 4.6, 7),
    (2, 6.3, 5),
    (3, 6.2, 1),
    (4, 4.4, 9),
    (5, 6.6, 4),
    (6, 5.8, 6),
    (1, 3.9, 7),
    (2, 3.1, 8),
    (3, 2.3, 9),
    (4, 1.5, 10),
    (5, 9.4, 1),
    (6, 8.6, 2),
    (1, 7.8, 3),
    (2, 7.0, 4),
    (2, 8.3, 2),
    (3, 7.2, 3),
    (4, 6.4, 4),
    (5, 5.6, 5),
    (6, 4.8, 6),
    (1, 3.9, 7),
    (2, 3.1, 8),
    (3, 2.3, 9),
    (4, 1.5, 10),
    (5, 9.4, 1),
    (6, 8.6, 2),
    (1, 7.8, 3),
    (2, 7.0, 4);
    '''
# verder uit te breiden
