import sqlite3

def select_all_products():
    with sqlite3.connect("store.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product")
        products = cursor.fetchall()
        return products

def select_product(id):
    with sqlite3.connect("store.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from Product where ProductID=?", (id,))
        product = cursor.fetchone()
        return product

if __name__ == "__main__":
    prod = select_all_products()
    print(prod)
    prod = select_product(3)
    print(prod)
