

"""
a=[1,2,3,4,5]

Rotate the elements by one left rotate

so first pass is
a=[2,3,4,5,1]

store the last element in temp

temp = a[0]
and then swap the previous elemenmt with the next one i-1 = i
"""

def left_rotate(nums):
    temp = nums[0]

    for i in range(1,len(nums)):
        nums[i-1] = nums[i]
    nums[len(nums)-1] = temp
    return nums

print(left_rotate([1,2,3,4,5]))