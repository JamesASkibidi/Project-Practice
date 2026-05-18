def Is_length_valid(value , minlength , maxlength = 64):
    if len(value)<minlength or len(value)>maxlength:
        return False
    return True
