input_values = input().split()
num1, num2 ,num3 ,num4 = input_values
num1 = int(num1)  # Convert string to integer
num2 = int(num2)  # Convert string to integer
num3 = int(num3)  # Convert string to integer
num4 = int(num4)  # Convert string to integer
difference = num1 * num2 - num3 * num4
print("Difference = " + str(difference))