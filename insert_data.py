import sqlite3

def insert_data(values):
    with sqlite3.connect('store.db') as db:
        cursor = db.cursor()
        sql = 'insert into Product (Name,Price) values (?,?)'
        cursor.execute(sql,values)
        db.commit()

if __name__ == '__main__':
    Product = ("Wooden Crate",20)
    insert_data(Product)
