# Import the regular expressions
import re
"""

This program will convert the binary code to decimals numbers

"""
# Catching the binary code
bCode = input('Write the binary code: ')


if len(bCode) > 8:
    # Verify the codeB, if the codeB variable has more than 8 digits, it will notify 
    print('You can digit only 8 digits, please try again!!')

    # Checking if there are any characters other than 0 and 1 using the
    # REGULAR EXPRESSIONS 
    binMod = re.search(r'[2-9A-Za-z]', bCode)
    if binMod == 'None':
        pass
    else:
        print('You used characters other than 0 and 1, please try again')

else:
    # Transforming the string(bCode) to a list
    binary = list(bCode)
    dec = 0

    # Mathematical logic
    for i in range(len(binary)):
        digit = binary.pop()
        if digit == '1':
            dec = dec + pow(2, i)
    print(f'The decimal value of the number is {dec}')
