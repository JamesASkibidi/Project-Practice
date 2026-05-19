import sqlite3 as sql

class DatabaseHandler:
    def __init__(self, database_name = "appData.db"):
        self.database_name = database_name

    def create_tables(self):
        cx = sql.connect(self.database_name)
        cu = cx.cursor()

        cu.execute("""

        CREATE TABLE IF NOT EXISTS user (
                   
                   username TEXT PRIMARY KEY NOT NULL
                   password TEXT NOT NULL,
                   CHECK( length(password) >= 8))
                   



""")

        cx.close()


    #CRUD

    def create_user(self):
        pass

    def retrieve_user(self):
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass