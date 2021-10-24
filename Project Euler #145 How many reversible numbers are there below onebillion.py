def contains_odds(number):
    for digit in number:
        if digit in "02468":
            return False
    return True

test_cases = int(input())

for test_case in range(test_cases):
    number = int(input())
    reversible = 0
    for num in range(1, number):
        if num % 10 != 0:
            reverse = int(str(num)[::-1])
            num_reverse_sum = num + reverse
            if contains_odds(str(num_reverse_sum)):
                reversible += 1
    print(reversible)