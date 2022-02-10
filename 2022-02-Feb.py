# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
# You're given one parameter, the original string. You don't have to worry with strings with less than two characters.


def remove_char(s):
    return s[1:-1]


print(f"REMOVE CHAR: {remove_char('IstringIUR')}")
# ------------------------------------

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.
# It should look like this:
# Sam Harris => S.H   ;    patrick feeney => P.F


def abbrev_name(name: str) -> str:
    return f'{name.split()[0][0].upper()}.{name.split()[1][0].upper()}'


print(f'ABBREV NAME: {abbrev_name("Hadim jedlicka")}')
# ------------------------------------

# Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).
# Examples:
# Input: [0]        Input: [0, 1, 4]        Input: [0, -1, -5]
# Output: "even"    Output: "odd"           Output: "even"


def odd_or_even(arr: list) -> str:
    """
    Function determines if the sum of a given list is odd or even.
    :param arr: list of integers
    :return: string 'odd' or 'even
    """
    if sum(arr) % 2 == 0:
        return 'even'
    else:
        return 'odd'
# or return 'even' if sum(arr) % 2 == 0 else 'odd'


print(f'ODD or EVEN: {odd_or_even([1,2,3,1])}')
# ------------------------------------

# Complete the solution so that it reverses the string passed into it.
# 'world'  =>  'dlrow'          # 'word'   =>  'drow'


def solution(string: str) -> str:
    return string[::-1]


print(f'Reversed string: {solution("ahoj")}')
# ------------------------------------

# Write a program that finds the summation of every number from 1 to num.
# The number will always be a positive integer greater than 0.

# For example:
# summation(2) -> 3         # summation(8) -> 36
# 1 + 2                     # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8


def summation(num):
    result = 0
    for number in range(num + 1):
        result += number
    return result
# or return sum(range(num + 1))


print(f'Summation: {summation(8)}')
# ------------------------------------

# Can you find the needle in the haystack?
# Write a function findNeedle() that takes an array full of junk but containing one "needle"
# After your function finds the needle it should return a message (as a string) that says:
# "found the needle at position " plus the index it found the needle, so:


def find_needle(haystack: list) -> str:
    index = haystack.index('needle')
    return f'found the needle at position {index}'


print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))
# ------------------------------------

# Complete the square sum function so that it squares each number passed into it and then sums the results together.
# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.


def square_sum(numbers):
    # result = 0
    # for number in numbers:
    #     result += number**2
    # return result
    return sum(number**2 for number in numbers)


print(f'Square_Sum: {square_sum([1, 2, 2])}')
# ------------------------------------
