#!/usr/bin/python3

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter your username : ")
    password = input("Enter your password : ")

    if username == "Doe" and password == "pa1@yuss":
        print("Login Successful")
        break
    else:
        attempts += 1
        print(f"Invalid username or password. {max_attempts - attempts} attempts left.")

if attempts == max_attempts:
    print("Maximum attempts reached, try again tomorrow")
