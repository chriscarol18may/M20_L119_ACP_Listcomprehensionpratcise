# 1. List comprehension for odd numbers under a user-input value
user_input = int(input("Enter a number: "))

# Using list comprehension to generate odd numbers below user_input
odd_numbers = [num for num in range(user_input) if num % 2 != 0]
print(f"Odd numbers below {user_input}: {odd_numbers}")

# 2. List comprehension to capitalize the first letter of each fruit in the list
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# Using list comprehension to capitalize the first letter of each fruit
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(f"Capitalized fruits: {capitalized_fruits}")