import sqlite3 as db
from sqlite3 import IntegrityError


class Person(object):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def to_string(self):
        return f'{self.name:<12} {self.email:<40} *****'


class PersonDatabase(object):
    def __init__(self, url):
        self.url = url        # location of database, automatically created if it doesn't exist
        self.connection = None  # connection to access database
        self.cursor = None      # pointer to current row

    def open(self):
        self.connection = db.connect(self.url)
        self.cursor = self.connection.cursor()

    def close(self):
        self.connection.commit()  # flush changes to disk if not already done
        self.connection.close()

    def fetch_all(self):
        results = []
        self.cursor.execute('''SELECT * FROM persons;''')
        for name, email, password in self.cursor.fetchall():
            results.append(Person(name, email, password))
        return results

    def create(self, person):
        create_query = """INSERT INTO persons (name, email, password) VALUES (?, ?, ?);"""
        self.cursor.execute(create_query, (person.name, person.email, person.password))
        self.connection.commit()

    def read(self, name):
        read_query = """SELET email, password FROM persons WHERE name = ?;"""
        self.cursor.execute(read_query, (name,))
        email, password = self.cursor.fetchone()
        return Person(name, email, password)

    def update(self, person):
        update_query = """UPDATE persons SET email = ?, password = ? WHERE name = ?"""
        self.cursor.execute(update_query, (person.email, person.password, person.name))
        self.connection.commit()

    def delete(self, key):
        delete_query = """DELETE FROM persons WHERE name = ?"""
        self.cursor.execute(delete_query, (key,))
        self.connection.commit()


def create_table_if_not_there(db_url):
    connection = db.connect(db_url)
    c = connection.cursor()
    create_table_query \
        = '''CREATE TABLE IF NOT EXISTS persons (name text NOT NULL unique, email text, password text )'''
    c.execute(create_table_query)
    connection.commit()
    connection.close()


def show_all_persons(database, message=''):
    print(f'Database contents {message}:')
    results = database.fetch_all()
    if not results:
        print('  Empty')
    else:
        for r in results:
            print(f'  {r.to_string()}')
    print()


def main():
    database_url = 'site.db'
    create_table_if_not_there(database_url)

    database = PersonDatabase(database_url)
    database.open()
    show_all_persons(database, 'at start')

    database.delete('bob')  # no exception if not there
    database.delete('sue')  # no exception if not there
    show_all_persons(database, 'after deleting')
    database.delete('bob')  # no exception if not there
    database.delete('sue')  # no exception if not there


    person = Person('bob', 'bob@bob.gmail', '*****')
    database.create(person)
    show_all_persons(database, 'after creating bob')

    try:
        database.create(person)
    except IntegrityError as e:
        print(f'Threw >{str(e)}< trying to create existing person\n')

    person.email = 'bobby@aol.com'
    database.update(person)
    show_all_persons(database, 'after updating')

    another_person = Person('sue', 'sue@gmail.com', str('-----'))
    database.create(another_person)
    show_all_persons(database, 'after adding sue')

    read_a_person = database.read('sue')
    print(f'read one row >{read_a_person.to_string()}<')
    database.close()

if __name__ == '__main__':
    main()