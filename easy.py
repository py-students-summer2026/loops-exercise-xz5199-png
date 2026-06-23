def one():
    """
    Write a program that prints the numbers from 1 to 10 using a for loop.
    """
    print("\neasy.one:")

    for i in range(1, 11):
        print('\t', i)

def two():
    """
    Write a program that prints the even numbers from 1 to 20 using a while loop.
    """
    print("\neasy.two:")
    i = 2
    while i <= 20:
        print('\t', i)
        i += 2

def three():
    """
    Write a program that calculates the sum of all numbers from 1 to 100 using a for loop.
    """
    print("\neasy.three:")

    sum = 0
    for i in range(1, 101):
        sum += i
    print('\t', sum)

def four():
    """
    Write a program that prints the first 10 multiples of 3 using a while loop.
    """
    print("\neasy.four:")

    i = 1
    while i <= 10:
        product = 3 * i
        print('\t', product)
        i += 1

def five(number):
    """
    Write a program that prints the factorial of a given number using a for loop. The factorial of a number is the product of all positive integers less than or equal to that number, e.g. 5! = 5 * 4 * 3 * 2 * 1 = 120.
    """
    print('\neasy.five:')

    product = number
    for i in range(number-1, 0, -1):
        product = product * i
    print('\t', f'{number} factorial = {product}')

def six(target):
    """
    Write a program that prints the Fibonacci sequence up to a given number using a while loop. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting from 0 and 1, e.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ....
    """
    print('\neasy.six:')

    second_to_last = 0
    last = 1
    print('\t', f'fibbonaci up to {target} = {second_to_last}, {last}', end='')
    while (last + second_to_last) <= target:
        total = last + second_to_last
        print(f', {total}', end='')
        second_to_last = last
        last = total
    print() # line break

def seven(text):
    """
    Write a program that counts the number of vowels in a given string using a for loop. The vowel letters are a, e, i, o, and u.
    """
    print('\neasy.seven:')

    total = 0
    for character in text:
        if character in ['a', 'e', 'i', 'o', 'u']:
            total += 1
    print('\t', f'# vowels in "{text}" = {total}')

def eight(number):
    """
    Write a program that checks if a given number is prime using a while loop. A prime number is a number greater than 1 that is only evenly divisible by 1 and itself.
    """
    print('\neasy.eight:')

    is_prime = True # assume it's prime
    divisor = number - 1
    while divisor > 1:
        if number % divisor == 0:
            is_prime = False
            break
        divisor -= 1
    
    if is_prime:
        print('\t', f'{number} is prime')
    else:
        print('\t', f'{number} is not prime... it is evenly divisible by {divisor}')
        
def nine():
    """
    Write a program that prints the ASCII values of all uppercase letters using a for loop. You may use the built-in ord() function to convert any character to its ASCII value.
    """
    print('\neasy.nine:')

    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('\t', end=' ')
    for letter in letters:
        if letter != 'Z':
            print(ord(letter), end=', ') # a comma after all letters except 'Z'
        else:
            print(ord(letter))

def ten(text):
    """
    Write a program that prints the reverse of a given string using a while loop.
    """
    print('\neasy.ten:')

    i = len(text) - 1
    print('\t', f'"{text}" backwards is "', end='')
    while i >= 0:
        print(text[i], end='')
        i -= 1
    print('"') # end quote and line break