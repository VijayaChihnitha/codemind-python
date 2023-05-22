def is_neon_number(num):
    square = num * num
    digit_sum = sum(int(digit) for digit in str(square))
    return digit_sum == num

# Test the function
num = int(input())
if is_neon_number(num):
    print("Neon Number")
else:
    print("Not Neon Number")
