import sqlite3
from sqlite3 import Error

 class _Wait:
     def __create_db(db_file):
         conn = None
         try:
             conn = sqlite3.connect(db_file):

