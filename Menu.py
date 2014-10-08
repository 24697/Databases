import sqlite3
from sql_database import *
from insert_data import *
from delete_data import *
from update_product import *
from serch_for_data import *


def main_menu():
    print("1. Create new database")
    print("2. Add data")
    print("3. Delete data")
    print("4. update existing data")
    print("5. Search database")
    print()
    print("Please sellect an option")

def get_input():
    correct = False
    while correct == False:
        try:
            option = int(input())
            if option 
    
