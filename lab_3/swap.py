
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


print("\n--- Before Swapping ---")
print(f"First number = {num1}")
print(f"Second number = {num2}")


num1, num2 = num2, num1


print("\n--- After Swapping ---")
print(f"First number = {num1}")
print(f"Second number = {num2}")