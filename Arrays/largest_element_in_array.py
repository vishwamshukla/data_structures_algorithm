"""
Find the largest element in the array

Brute Force
Optimized
Most optimal solution

a=[3,2,1,5,2]

The largest in this array is 5
"""

"""
Brute Force Approach

Sort the array
a=[1,2,2,3,5]

and print the last element

Time - O(NlogN)
Space - O(1)
"""
"""
Optimal solution is to traverse the array and have O(N) as time complexity
"""

a=[3,2,1,5,2]

def find_largest_brute_force(array):
    largest = array[0]
    for i in range(len(array)):
        if(array[i] > largest):
            largest = array[i]
    return largest
print(find_largest_brute_force([3,2,1,5,2]))
