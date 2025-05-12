# # #alexander johnson
# # 4-26-25
# # Loop that shows numbers multiplied by a range going from 1-10


while True:
    # Get user input for the integer
    num = int(input("Enter a positive integer: "))
    
    # Check if the number is positive, if not, ask again
    if num <= 0:
        print("Please enter a positive number.")
        continue  # Skip this iteration and ask for input again
    
    # Define the range for multipliers
    start = 1
    end = 13  # This will make the multiplier go from 1 to 10 (inclusive)
    
    # Loop through the multiplier range
    for multiplier in range(start, end):
        result = num * multiplier
        print(f"{num} * {multiplier} = {result}")
    
    # Ask if the user wants to continue
    continue_response = input("Do you want to continue? (y/n): ").lower()
    
    if continue_response != 'y':  # If not 'y', exit the loop
        break  # Exit the loop