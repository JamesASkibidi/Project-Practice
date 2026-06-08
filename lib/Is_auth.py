





from flask import session


def Is_auth():
    print(session.get("current_user"))
    return session.get("current_user") != None 
