# Name: Alex Johnson
# Date: 04/19/2025
# Assignment Name: p1hw2
# Description: This program calculates and displays travel expenses.

budget = float(input("Enter Budget: "))
destination = input("\nEnter your travel destination: ")

gas = float(input("\nHow much do you think you will spend on gas? "))
accommodation = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("\nFuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print("\nRemaining Balance:", remaining_balance)

input()
