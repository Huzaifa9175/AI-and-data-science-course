# 1. Check if number is positive, negative, or zero
num = float(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Find larger of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if a > b:
    print("Larger number is:", a)
elif b > a:
    print("Larger number is:", b)
else:
    print("Both are equal")

# 3. Find largest of three numbers
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
if x >= y and x >= z:
    print("Largest is:", x)
elif y >= x and y >= z:
    print("Largest is:", y)
else:
    print("Largest is:", z)

# 4. Check if string “Mass” is in “Saylani Mass IT”
if "Mass" in "Saylani Mass IT":
    print("String found")

# 5. Age categorization
age = int(input("Enter your age: "))
if age < 18:
    print("Minor")
elif 18 <= age < 60:
    print("Adult")
else:
    print("Senior Citizen")

# 6. Even or Odd
num = int(input("Enter an integer: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 7. Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, x, /): ")
if op == '+':
    print("Result:", num1 + num2)
elif op == '-':
    print("Result:", num1 - num2)
elif op == 'x':
    print("Result:", num1 * num2)
elif op == '/':
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operator")

# 8. Check if number in range 20–40
num = int(input("Enter a number: "))
if 20 <= num < 40:
    print("Number is in the range 20–40")
else:
    print("Number is outside the range")

# 9. Divisibility check
num = int(input("Enter an integer: "))
if num % 2 == 0 and num % 3 == 0:
    print("Divisible by both 2 and 3")
elif num % 2 == 0:
    print("Divisible by 2")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 2 or 3")

# 10. Pass or Fail
score = float(input("Enter your score: "))
if score > 60:
    print("Pass")
else:
    print("Fail")

# 11. Prime Number Check
num = int(input("Enter a number: "))
if num <= 1:
    print("Not Prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")

# 12. Temperature Check
temp = float(input("Enter temperature in Celsius: "))
if temp < 0:
    print("Freezing")
elif 0 <= temp < 26:
    print("Moderate")
else:
    print("Hot")
