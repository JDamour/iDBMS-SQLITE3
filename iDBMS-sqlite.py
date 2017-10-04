#!/usr/bin/env python3

from database import database

def main():
    db = database(filename = ':memory:', table = 'table_name')

    print('Create table table_name')
    db.sql_do('drop table if exists table_name')
    db.sql_do('create table table_name ( col1 int, col2 text, col3 text, coln text )')

    print('Create rows')
    db.insert(dict(col1 = 1, col2 = 'one', col3 = 'first', coln = 'One is inserted'))
    db.insert(dict(col1 = 2, col2 = 'two', col3 = 'second', coln = 'Two is inserted'))
    db.insert(dict(col1 = 3, col2 = 'three', col3 = 'third', coln = 'Three is inserted'))
    db.insert(dict(col1 = 4, col2 = 'four', col3 = 'fourth', coln = 'Four is inserted'))
    db.insert(dict(col1 = 5, col2 = 'five', col3 = 'fifth', coln = 'Five is inserted'))
    for row in db: print(row)

    print('Retrieve rows')
    print(db.retrieve(1), db.retrieve(2))


if __name__ == "__main__": main()
