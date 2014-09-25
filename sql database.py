import sqlite3

def create_table(db_name,table_name,sql):
    with sqlite3.connect(db_name)as db:
        cursor = db.cursor()
        cursor.execute('select name from sqlite_master where name = ?',(table_name,))
        result = cursor.fetchall()
        keep_table = True
        if len(result) == 1:
            responce = input('The Table {0} already exists, do you want to recreate the table (y/n): '.format(table_name))
            if responce == 'y':
                keep_table = False
                print('The {0} table will be recreated - all existing data will be lost'.format(table_name))
                cursor.execute('drop table if exists {0}'.format(table_name))
            else:
                print('The table was kept')
        else:
            keep_table = False
        if not keep_table:
            cursor.execute(sql)
            db.commit()



if __name__ == '__main__':
    db_name = 'store.db'
    sql = """create table Product(
    ProductID interger, 
    Name text, 
    Price real, 
    Primary Key(ProductID))"""
    create_table(db_name,'Product',sql)
