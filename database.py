import sqlite3 as sql

class DatabaseHandler:
    def __init__(self, database_name = "appData.db"):
        self.database_name = database_name

    def create_tables(self):
        cx = sql.connect(self.database_name)
        cu = cx.cursor()

        cu.execute("""

        CREATE TABLE IF NOT EXISTS user (
                   
                   u_id INTEGER PRIMARY KEY AUTOINCREMENT,          
                   username TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL,
                   email TEXT,
                   CHECK( length(password) >= 8))
                

""")

        cx.close()


    #CRUD

    def create_user(self , username, password, email):
        try:
            cx = sql.connect(self.database_name)
            cu = cx.cursor()
            


            cu.execute("""INSERT INTO user (username, password, email) VALUES (?,?,?)""", (username, password, email))
            cx.commit()


            
            return True , "account succesfully created"
        except:
            return False, "an error has occured"
        finally:
            cx.close

    def retrieve_user(self , username):
        
        pass

    def update_user(self):
        pass

    def delete_user(self):
        pass

    def find_password(self, username):
        try:
            cx = sql.connect(self.database_name)
            cu = cx.cursor()
            

            cu.execute("""SELECT password FROM user WHERE username = ?""" , (username, ))


            results = cu.fetchone()
            
            print(results)
            return True, results
        except:
            return False ,"Authentication Failure"
        finally:
            cx.close()
