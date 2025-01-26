"""
Find the second largest element in the array
a=[1,2,4,7,7,5]
Once sorted 1,2,4,5,7,7 the second largest is 5 not 7
 time for sorting is O(nlogn)
 and then traverse the array again to find the second largest  worst case can be O(n) in some cases the second largest doesnt exists so keep it to -1

 so the solution is of O(nlogn) + O(n)

 Another solution is

 to Find the largest first and then find the second largest element in the array
"""

def find_second_largest(a): #O(NlogN)
    a.sort()
    largest=a[-1]
    for i in range(len(a)-2,0,-1):
        if a[i] < largest:
            return a[i]
    return None


def find_second_largest_optimal(a): #O(N+N)
    largest=a[0]
    for i in range(len(a)):
        if a[i] > largest:
            largest = a[i]
    second_largest=-1
    for i in range(len(a)):
        if a[i] > second_largest and a[i] != largest:
            second_largest=a[i]
    return second_largest

print(find_second_largest([1,2,4,7,7,5]))


def find_second_largest_optimzed_3(a): #O(N)
    largest=a[0]
    second_largest = -1

    for i in range(len(a)):
        if (a[i] > largest):
            largest = a[i]
            second_largest=largest
    return second_largest
print(find_second_largest([1,2,4,7,7,6]))