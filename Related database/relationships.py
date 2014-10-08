import sqlite3

with sqlite3.connect("new_store.db") as db:
    cursor = db.cursor()
    sql = """create table ProductType(
          ProductTypeID integer,
          ProductDiscription text,
          Primary Key(ProductTypeID))"""
    cursor.execute(sql)
    sql = """create table Product(
          ProductID integer,
          Name text,
          Price real,
          ProductTypeID integer,
          Primary Key(ProductID),
          foreign Key(ProductTypeID) referances ProductType(ProductTypeID)"""
    cursor.execute(sql)
