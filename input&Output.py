print("Welcome to system terminal")
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the system terminal.")
age_str = input("Enter your age: ")

try:
    age = int(age_str)
    print(f"Hello, {name}! You are {age} years old.")
except ValueError:
    print("Invalid age. Please enter a valid integer.")
    exit(1)
