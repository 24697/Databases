import sqlite3

def update_product(data):
    with sqlite3.connect("store.db") as db:
        cursor = db.cursor()
        sql = "update Product set Name=?,Price = ? where ProductID = ?"
        cursor.execute(sql,data)

if __name__ == '__main__':
    data = ("recenfored wooden crate",25.55,0)
    update_product(data)
