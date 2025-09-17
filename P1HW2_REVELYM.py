# Revely Monique    
# 9/17/2025
# Idle
# The goal of this assignment is to practice working with user input, 
# basic math functions, and conditional statements using IDLE.

# Step 1: Ask user to enter their budget
budget = float(input("Enter your travel budget: $"1000))

# Step 2: Ask user to enter travel destination
destination = input("Enter your travel destination: "hawaii)

# Step 3: Ask user for amount they will spend on gas
gas_expense = float(input("Enter amount you will spend on gas: $200"))

# Step 4: Ask user for amount they will spend on accommodation
accommodation_expense = float(input("Enter amount you will spend on accommodation: $500"))

# Step 5: Ask user for amount they will spend on food
food_expense = float(input("Enter amount you will spend on food: $150"))

# Step 6: Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Step 7: Subtract expenses from budget
remaining_budget = budget - total_expenses

# Step 8: Display results
print("\n--- Travel Budget Summary ---")
print(f"Destination: {destination}")
print(f"Total Budget: ${budget:.2f}")
print(f"Gas Expense: ${gas_expense:.2f}")
print(f"Accommodation Expense: ${accommodation_expense:.2f}")
print(f"Food Expense: ${food_expense:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")

# Check if the remaining budget is negative (user has overspent)
if remaining_budget < 0: 150
    print("\nWarning: You have exceeded your budget!")
else:
    print("\nYou are within your budget!")
