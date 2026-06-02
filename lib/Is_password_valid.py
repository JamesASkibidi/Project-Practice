

from lib.Is_length_valid import Is_length_valid

def Is_password_valid(value):

    if not Is_length_valid(value , 8):
        return False , "Password must be between 8 and 64 characters in length"
    
    s_c = False
    num = False
    upper = False
    lower = False
    
    for char in value:
        if ord(char)<33:
            return False, "invalid Characters"
        if  (ord(char) >32 and  ord(char)<48):s_c = True
        if ord(char)>47 and ord(char)<58: num = True
        if ord(char)>40 and ord(char)<91: upper = True
        if ord(char)>96 and ord(char)<123: lower = True
    if s_c and num and upper and lower:
        return True , "All requirements met"
    
    return False, "Please use at least 1 Uppercase letter, 1 Lowercase Letter, 1 special character and 1 number"
    
    