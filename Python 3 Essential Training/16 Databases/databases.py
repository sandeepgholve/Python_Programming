#!/usr/bin/python3

import sqlite3

def main():
    db = sqlite3.connect('test.db')
    db.execute('drop table if exists test')
    db.execute('create table test(t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('Sandeep', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('Anita', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('Aarohi', 3))
    db.execute('insert into test (t1, i1) values (?, ?)', ('Rihan', 4))
    db.commit()
    
    cursor = db.execute('select * from test order by t1')
    for row in cursor:
        print(row)
    
        
if __name__ == "__main__" : main()