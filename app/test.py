#!/usr/bin/env python
# coding: utf-8
# Author: huangchao

if __name__ == '__main__':

    import sqlite3, os

    basedir = os.path.abspath(os.path.dirname(__file__))


    conn = sqlite3.connect('/Users/huangchao/PycharmProjects/flaskr/data.sqlite')
    cur = conn.cursor()

    cur.execute("insert into students values(1,'Allen',1)")
    cur.execute("insert into students values(2,'Bob',2)")
    cur.execute("insert into students values(3,'Tina',1)")

    cur.execute("insert into classes values(1,'class1')")
    cur.execute("insert into classes values(2,'class2')")

    cur.close()
    conn.commit()
    conn.close()
