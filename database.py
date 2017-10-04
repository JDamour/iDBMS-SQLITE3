#!/usr/bin/env python3

import sqlite3

class database:
    def __init__(self, **kwargs):
        self.filename = kwargs.get('filename')
        self.table = kwargs.get('table', 'table_name')

    def sql_do(self, sql, *params):
        self._db.execute(sql, params)
        self._db.commit()

# Insert method allows to insert record in db
    def insert(self, row):
        self._db.execute('insert into {} (col1, col2, col3, coln) values (?, ?, ?, ?)'.format(self._table), (row['col1'], row['col2'], row['col3'], row['coln']))
        self._db.commit()

    # Retrieve row data in memory database
    def retrieve(self, key):
        cursor = self._db.execute('select * from {} where col1 = ?'.format(self._table), (key,))
        return dict(cursor.fetchone())

    def __iter__(self):
        cursor = self._db.execute('select * from {} order by col1'.format(self._table))
        for row in cursor:
            yield dict(row)

    @property
    def filename(self): return self._filename

    @filename.setter
    def filename(self, fn):
        self._filename = fn
        self._db = sqlite3.connect(fn)
        self._db.row_factory = sqlite3.Row

    @property
    def table(self): return self._table

    @table.setter
    def table(self, t): self._table = t

    @table.deleter
    def table(self): self._table = 'table_name'

    def close(self):
            self._db.close()
            del self._filename