import sqlite3

def update_product(data):
    with sqlite3.connect("store.db") as db:
        cursor = db.cursor()
<<<<<<< HEAD
        sql = "update Product set Name = ?, Price = ? where ProductID = ?"
        cursor.execute(sql,data)
        db.commit()

if __name__ == "__main__":
    data = ("New Box",25,1)
=======
        sql = "update Product set Name=?,Price = ? where ProductID = ?"
        cursor.execute(sql,data)

if __name__ == '__main__':
    data = ("recenfored wooden crate",25.55,0)
>>>>>>> branch 'master' of https://github.com/24697/Databases.git
    update_product(data)
