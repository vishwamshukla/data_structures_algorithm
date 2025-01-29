"""
Left rotate the array by D places

a=[1,2,3,4,5,6,7] d=2

result = [3,4,5,6,7,1,2]

If rotate with it's len value i.e 7 then the same answer as array a

if 8 then 7+1, so its only one rotation

So the rotation will be D=D modulu N - modulo operation which result the remainder. we have to rotate the array by the remainder

Brute force

If D, we will store the number of D elements
If D=2, then first two elements will be stored in temp and then we will rotate the remaining elements back

Optimal solution

1. Reverse the first array of set D
2. Reverse the second set of the array
3. Reverse the entire array
"""

def rotate_by_d(nums, k):
    n = len(nums)
    k = k % n
    nums[:n - k] = nums[:n - k][::-1]
    nums[n - k:] = nums[n - k:][::-1]

    nums.reverse()
    return nums

print(rotate_by_d([1,2,3,4,5,6,7], 3))