import re

# from email_validator import validate_email, EmailNotValidError

'''Write a python program to validate the details provided by a user as part of registering to a web application.

Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets
'''
# name=input("name:")
# def validate_name(name):
#     if len(name) > 15 :
#         print("enter name under 15 letters")
#         return False
#     valid_name = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
#     for ch in name:
#         if ch() not in valid_name:
#             return False
#     return True
# validate_name(name)


# phno=input("Enter the phone number: ")
# def validate_phone_no(phno):
#     if len(phno) <10 \
#         and phno[:].isdigit():
#         return False
#     print("Invalid Phone Number")
#     return True
# validate_phone_no(phno)


# email_id=input("email: ")
# def validate_email_id(email_id):
#     pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     if re.match(pat,email_id):
#         print("Valid Email")
#         return True
#     else:
#         print("Invalid Email")
#         return False
# validate_email_id(email_id)


# def validate_all(name,phno,email_id):
#     if validate_name(name) is False:
#         print("Invalid Name")
#     if validate_phone_no(phno) is False:
#         print("Invalid phone number")
#     if validate_email_id(email_id) is False:
#         print("Invalid email id")
#     else:
#         print("All the details are valid")


# # validate_all("Tina", "9994599998", "tina@yahoo.com")