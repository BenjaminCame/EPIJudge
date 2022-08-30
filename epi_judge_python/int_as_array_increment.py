from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    A[-1] += 1 #-1 indexes the last element of the sequence 
    for index in reversed(range(1,len(A))):        
        if A[index] != 10: # no more opperations needed
            break
        else:
            A[index] = 0
            A[index - 1] += 1
    if A[0] == 10: #there is a carry
        A[0] = 1
        A.append(0)



    for num in A:
        print(num)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
