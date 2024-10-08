from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = -1 if num1[0] ^ num2[0] < 0 else 1
    result = [0] * (len(num1) + len(num2))
    num1[0] , num2[0] = abs(num1[0]), abs(num2[0])

    # max calculation is 9 * 9 = 81
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            # calculate into the 1's column
            result[i + j + 1] += num1[i] * num2[j]
            # add the value to the 10's column and foor devide out the one's column  
            result[i + j] += result[i + j + 1] // 10 
            # use modulo to remove the 10's value from the units 
            result[i + j + 1] %= 10 

    # remove leading zeros
    result = result[next((i for i, x in enumerate(result)
                          if x != 0), len(result)):] or [0]

    # correct the sign of the first element
    result[0] = result[0] * sign

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
