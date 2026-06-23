def one():
    print("\ndifficult.one:")
    number = 79
    original = number
    factors = []
    import math
    for i in range(2, int(math.sqrt(number)) + 1):
        while number % i == 0:
            factors.append(i)
            number = number // i
    if number > 1:
        factors.append(number)
    print('\t', f'the prime factors of {original} are {factors}')

def two():
    print("\ndifficult.two:")
    n = 10  
    if n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        a = 0  
        b = 1  
        count = 2   
        while count <= n:
            c = a + b
            a = b
            b = c
            count += 1
        result = b
    print('\t', f'the {n}th term of Fibonacci sequence is {result}')

def three():
    print("\ndifficult.three:")
    word1 = "hello"
    word2 = "world"
    if len(word1) != len(word2):
        print('\t', f'"{word1}" and "{word2}" are not anagrams')
        return
    count1 = {}
    for char in word1:
        if char in count1:
            count1[char] += 1
        else:
            count1[char] = 1
    count2 = {}
    for char in word2:
        if char in count2:
            count2[char] += 1
        else:
            count2[char] = 1
    if count1 == count2:
        print('\t', f'"{word1}" and "{word2}" are anagrams')
    else:
        print('\t', f'"{word1}" and "{word2}" are not anagrams')

def four():
    print("\ndifficult.four:")
    first_term = 2
    common_difference = 3
    n = 10    
    term = first_term
    count = 1
    print('\t', f'first {n} terms of arithmetic sequence (difference = {common_difference}):')
    print('\t', term, end='') 
    count = 2
    while count <= n:
        term = term + common_difference
        print(f', {term}', end='')
        count += 1

def five():
    print("\ndifficult.five:")
    numbers = [3, 1, 4, 8, 5, 9, 2, 6, 4]
    original = numbers.copy()  
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    if n % 2 == 1:  
        middle_index = n // 2
        median = numbers[middle_index]
        print('\t', f'the median of {original} is {median}')
    else:          
        middle_index1 = n // 2 - 1
        middle_index2 = n // 2
        median = (numbers[middle_index1] + numbers[middle_index2]) / 2
        print('\t', f'the median of {original} is {median}')

def six():
    print("\ndifficult.six:")
    number = 28
    divisor_sum = 0
    i = 1
    while i <= number // 2:  
        if number % i == 0:
            divisor_sum += i
        i += 1
    if divisor_sum == number:
        print('\t', f'{number} is a perfect number')
        print('\t', f'{number} = 1 + 2 + 4 + 7 + 14 = {divisor_sum}')
    else:
        print('\t', f'{number} is not a perfect number')

def seven():
    print("\ndifficult.seven:")
    number = 12345
    digit_sum = 0
    print('\t', f'{number} = ', end='')
    for i, char in enumerate(str(number)):
        digit = int(char)
        digit_sum += digit 
        if i > 0:
            print(f' + {digit}', end='')
        else:
            print(digit, end='')
    print(f' = {digit_sum}')

def eight():
    print("\ndifficult.eight:")
    sentence = "It is raining heavily today."
    words = sentence.split()
    longest_word = words[0]
    longest_length = len(words[0])
    i = 1
    while i < len(words):
        if len(words[i]) > longest_length:
            longest_word = words[i]
            longest_length = len(words[i])
        i += 1
    print('\t', f'longest word in "{sentence}" is "{longest_word}" ({longest_length} letters)')

def nine():
    print("\ndifficult.nine:")
    sentence = "It is raining heavily today."
    lower_sentence = sentence.lower()
    letters = set() 
    for char in lower_sentence:
        if 'a' <= char <= 'z':  
            letters.add(char)
    if len(letters) == 26:
        print('\t', f'"{sentence}" is a pangram')
        print('\t', f'it contains all 26 letters: {sorted(letters)}')
    else:
        missing = []
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            if letter not in letters:
                missing.append(letter)
        print('\t', f'"{sentence}" is not a pangram')
        print('\t', f'missing letters: {missing}')

def ten():
    print("\ndifficult.ten:")
    number = 2
    primes = []
    while number <= 1000:
        prime = True
        divisor = 2
        while divisor * divisor <= number:
            if number % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            primes.append(number)   
        number += 1
    print('\t', f'there are {len(primes)} prime numbers between 1 and 1000')
    print('\t', f'they are: {primes}')