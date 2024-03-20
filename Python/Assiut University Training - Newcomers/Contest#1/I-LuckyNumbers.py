def is_lucky(number):
    # Extract the digits
    tens_digit = number // 10
    ones_digit = number % 10
    
    # Check if one digit is divisible by the other
    if tens_digit == 0 or ones_digit == 0:
        return "YES"  # Zero cannot be a divisor
    if tens_digit % ones_digit == 0 or ones_digit % tens_digit == 0:
        return "YES"
    else:
        return "NO"

# Read input
N = int(input().strip())

# Check if the number is lucky and print the result
print(is_lucky(N))
