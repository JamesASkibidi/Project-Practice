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
                   CHECK( length(password) >= 8)
                   )
                    """)

        cu.execute("""
                
        CREATE TABLE IF NOT EXISTS task (
                   
                   t_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   description TEXT NOT NULL, 
                   u_id INTEGER NOT NULL,
                   CHECK (length(description) >= 3),
                   FOREIGN KEY (u_id) REFERENCES user(u_id)
                   ON DELETE CASCADE
                   ON UPDATE CASCADE
                   
                   )
                   """)#cascades endure that any changes to the foreign key effect all references
        
        cu.execute("PRAGMA foreign_keys = ON")#activates functionmality for foreign key functions

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

    def create_task(self, description, u_id):
        
        try:
            cx = sql.connect(self.database_name)
            cu = cx.cursor()

            cu.execute("""
                INSERT INTO TASK (description, u_id)
                VALUES (? ,?)""" , (description, u_id))

            cx.commit()

            return True, "Task created"

        except:

            return False , "An error has occured"
   
        finally:
            cx.close()

    def retreive_tasks(self, u_id):

        try:

            cx = sql.connect(self.database_name)
            cu = cx.cursor()

            cu.execute("""
                       SELECT t_id, descrition
                       FROM task WEHRE u_id = ?""" , (u_id))
            results = cu.fetchall()

            return True, results
            

        except:

            return False, []



            
        finally:

            cx.close()
        
        