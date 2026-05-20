

from lib.Is_length_valid import Is_length_valid

def Is_password_valid(value):

    if not Is_length_valid(value , 8):
        return False
    
    for char in value:
        if ord(char)>32 and ord(char)<65:
            return True
    
    