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
