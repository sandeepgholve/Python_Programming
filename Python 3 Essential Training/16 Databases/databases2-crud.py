#!/usr/bin/python3

import sqlite3

def insert(db, row):
    db.execute('insert into test (t1, i1) values (?, ?)', (row['t1'], row['i1']))
    db.commit()

def retrieve(db, t1):
    cursor = db.execute('select * from test where t1 = ?', (t1,))
    return cursor.fetchone()

def update(db, row):
    db.execute('update test set i1 = ? where t1 = ?', (row['i1'], row['t1']))
    db.commit()

def delete(db, t1):
    db.execute('delete from test where t1 = ?', (t1,))
    db.commit()
    
def disp_rows(db):
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print('  {}: {}'.format(row['t1'], row['i1']))

def main():
    db = sqlite3.connect('test1.db')
    db.row_factory = sqlite3.Row
    print('Create table test')
    db.execute('drop table if exists test')
    db.execute('create table test(t1 text, i1 int)')

    print('Create Rows')
    insert(db, dict(t1 = 'Sandeep', i1 = 1))
    insert(db, dict(t1 = 'Anita', i1 = 2))
    insert(db, dict(t1 = 'Aarohi', i1 = 3))
    insert(db, dict(t1 = 'Rihan', i1 = 4))
    disp_rows(db)

    print('Retrieve Rows')
    print(dict(retrieve(db, 'Sandeep')), dict(retrieve(db, 'Anita')))

    print('Update Rows')
    update(db, dict(t1 = 'Sandeep', i1 = 101))
    print(dict(retrieve(db, 'Sandeep')))
    
    print('Delete Rows')
    delete(db, 'Anita')
    
    disp_rows(db)
if __name__ == "__main__" : main()