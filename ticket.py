#!/usr/bin/python3

while True:
    try:
        age = int(input("Please enter your age : "))
        break

    except ValueError:
        print("Invalid input. Please, try again")

if age <= 17:
    print("Ticket amount : GH₵ 30.00")

elif 17 <= age <= 60:
    print("Ticket amount : GH₵ 50.00")

else:
    print("Ticket amount : GH₵ 40.00")
