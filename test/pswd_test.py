from lib.Is_password_valid import Is_password_valid


password = input("enter password")


# success , message = Is_password_valid(password)


if not Is_password_valid(password):
    print("fail")