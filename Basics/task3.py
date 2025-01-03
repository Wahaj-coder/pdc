def greet(name):
    return f"Hello, {name}!"

def calculate_square(num):
    return num * num

# Example usage
name = input("Enter your name: ")
print(greet(name))

number = float(input("Enter a number to calculate its square: "))
print(f"The square of {number} is {calculate_square(number)}")
