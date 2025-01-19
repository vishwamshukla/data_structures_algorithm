'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''


'''

1. Understand the problem

Array and an integer target

Return the indices of two numbers such that they add up to target

array = [1,2,3,4] Suppose we have Target as 5

[1,2] - Sum of 2+3=5

Constraints  - Only one solution exists. cant use the same element twice and can we come up with an algo that is less than O(n^2) time.

'''

'''
Brute Force Approach

array = [1,2,3,4] Suppose we have Target as 5

- Iterate through the array as the outer loop
- Another inner loop to select second number in the pair

- Inside the inner loop, check the sum of two selected numbers equals the target and return indices

'''

# Brute Force Approach
'''
nums = [1,2,3,4]
target = 5
i = 1
j=2
3

-----
i=2
j=3

5
return [i,j]

'''

def twoSumBruteForce(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

print(twoSumBruteForce([2,7,11,15], 9))

'''
Time Complexity

- Outer loop runs for n times
- Inner loop runs for n-1
- Total - O(nxn) = O(n^2)

Space Complexity

No additional data structures are used

- O(1)
'''




'''
Optimal Solution

- Using Hashmap

Use hashmap to store the difference (target - current element) as the key and the index of the current element as the value
Iterate through array and check the current element exists in hashmap

- Create a hashmap
- Iterate through array with i and value of num
- For each element - diff = target - num - check if exists in hashmap if yes return indices of hashmap and i
if no store hashamp with num = i

nums = [2,7,11,15]
target = 9

hasmap = {}

first iteration = i=0, num=2

diff = target - num = 9-2 = 7 - doesnt exsist in hashmap

so store store num in hasmap  - hasmap{2:0}

next iteration

i=1, num = 7

diff = 9-7 = 2
2 is in hasmap so return hasmap's indice of 2 and i

[0,1]

time = iterate the array - O(n) x hashmap's ops are O(1) so O(n)
space - storing the hashmap elements is O(n)
'''

def twoSumHashMap(nums, target):
    hashmap = {} # O(n) space

    for i, num in enumerate(nums):  # O(n) time

        diff = target - num

        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i



print(twoSumHashMap([2,7,11,15], 9))



'''
2, 7, 11, 15 Target = 9

1. i=0, num = 2

diff = 7

dict = {2:0}

2. i=1, num = 7

diff = 2

exists in hashmap

return dict[diff, i]

'''

