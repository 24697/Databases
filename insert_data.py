import sqlite3

def insert_data(values):
    with sqlite3.connect("store.db") as db:
        cursor = db.cursor()
        sql = "insert into Product (Name,Price) values(?,?)"
        cursor.execute(sql,values)
        db.commit

if __name__ == "__main__":
    values = ('Box',5)
    insert_data(values)
    values = ('New Box',10)
    insert_data(values)
    values = ('Pink Sippers',2)
    insert_data(values)
    values = ('Green Gem',20)
    insert_data(values)
    values = ('Golden Tablet',100000000000)
    insert_data(values)
