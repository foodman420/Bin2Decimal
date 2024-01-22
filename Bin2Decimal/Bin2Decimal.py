
def bin_to_dec(binary): 
    decimal = 0
    for position, digit in enumerate(reversed(binary)):
        if digit == '0':
            continue
        elif digit == '1':
            decimal += 2 ** position
        else:
            raise ValueError("Binary digit must be 0 or 1")
        
    return decimal

binary_input = input("Enter a binary number of up to 8 digits: ")
 
if len(binary_input) <= 8 and all(digit in '01' for digit in binary_input):
    decimal_result = bin_to_dec(binary_input)
    print(f"The decimal equivalent of {binary_input} is {decimal_result}")
else:
    print("Invalid input. Please enter a binary number of up to 8 digits.")