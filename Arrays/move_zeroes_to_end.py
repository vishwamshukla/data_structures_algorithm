"""

move all the zeroes to the end of the array

a=[1,0,2,3,0]

result = [1,2,3,0,0]

Brute force

temp to store non zero number and add to this array

now put back all the temp elements to the array

Fill the zeroes from the end of the temp size

OPtimal

two pointers

i to keep track of non zero
j to keep track of zeroes and swap them
"""


"""
Brute force approach

1. Store all the non zero elements in a different array temp
2. Put all the elements from temp array to the main array and place them in front of the array

1 0 2 3 2 0 0 4 5 1

1 2 3 2 4 5 1 - temp

1 2 3 2 4 5 1 0 0 0

But the time is O(N) and Space is O(N)

"""

def move_zeroes(nums):
    j=0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

print(move_zeroes([0,1,0,3,12]))