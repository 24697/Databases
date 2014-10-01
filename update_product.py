import sqlite3

def update_product(data):
    with sqlite3.connect("store.db") as db:
        cursor = db.cursor()
        sql = "update Product set Name = ?, Price = ? where ProductID = ?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = ("New Box",25,1)
    update_product(data)
