def one():
    print("\n medium one: ")
    numbers = [4, 5, 1, 0, 7, 8]
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    print('\t', f'the largest number in {numbers} is {largest}')
    
def two():
    print("\nmedium.two:")
    numbers = [10, 20, 30, 40, 60]
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1 
    average = total / len(numbers)
    print('\t', f'the average of {numbers} is {average}')

def three():
    print("\nmedium.three:")
    text = "radar"
    is_palindrome = True
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - 1 - i]:
            is_palindrome = False
            break
    if is_palindrome:
        print('\t', f'"{text}" is a palindrome')
    else:
        print('\t', f'"{text}" is not a palindrome')

def four():
    print("\nmedium.four:")
    first_term = 2
    common_ratio = 2
    n = 10    
    term = first_term
    count = 1
    print('\t', f'first {n} terms of geometric sequence (ratio = {common_ratio}):')
    print('\t', term, end='')
    count = 2
    while count <= n:
        term = term * common_ratio
        print(f', {term}', end='')
        count += 1

def five():
    print("\nmedium.five:")
    numbers = [3, 7, 1, 9, 4, 6, 8]
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    second_largest = float('-inf')
    for num in numbers:
        if num != largest and num > second_largest:
            second_largest = num
    
    print('\t', f'in {numbers}, the second largest number is {second_largest}')

def six():
    print("\nmedium.six:")
    number = 5
    factorial = 1
    i = number
    while i > 0:
        factorial = factorial * i
        i = i - 1
    print('\t', f'{number}! = {factorial}')

def seven():
    print("\nmedium.seven:")
    number = 49
    square = False
    for i in range(1, number + 1):
        if i * i == number:
            square = True
            break
        elif i * i > number:
            break
    if square:
        print('\t', f'{number} is a perfect square (√{number} = {int(number ** 0.5)})')
    else:
        print('\t', f'{number} is not a perfect square')

def eight():
    print("\nmedium.eight:")
    total = 0
    number = 2
    while number <= 100:
        prime = True
        divisor = 2
        while divisor <= number // 2:
            if number % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            total += number
        number += 1
    print('\t', f'the sum of all prime numbers between 1 and 100 is {total}')

def nine():
    print("\nmedium.nine:")

    sentence = "Oh no! Is it raining heavily now?"
  
    separators = [',', '.', '!', '?', ';', ':', '(', ')']
    cleaned = sentence
    for sep in separators:
        cleaned = cleaned.replace(sep, ' ')
    words = cleaned.split()
    count = len(words)
    print('\t', f'"{sentence}" has {count} words')

def ten():
    print("\nmedium.ten:")
    list1 = [1, 7, 3, 4, 5, 6]
    list2 = [3, 5, 6, 7, 8, 9]
    common = []
    i = 0
    while i < len(list1):
        j = 0
        found = False
        while j < len(list2):
            if list1[i] == list2[j]:
                found = True
                break
            j += 1
        if found:
            common.append(list1[i])
        i += 1 
    print('\t', f'common elements between {list1} and {list2} are {common}')