import math
input_values = input().split()
num1, num2 = map(int, input_values)
# Calculate division
x = num1 / num2
# Floor division
floor_result = math.floor(num1 / num2)
print("floor", num1, "/", num2, "=", floor_result)
# Ceiling division
ceil_result = math.ceil(num1 / num2)
print("ceil", num1, "/", num2, "=", ceil_result)
# Determine whether to round up or down
dif = x - math.floor(x)
if dif < 0.5:
    print("round", num1, "/", num2, "=", math.floor(x))
else:
    print("round", num1, "/", num2, "=", math.floor(x) + 1)
