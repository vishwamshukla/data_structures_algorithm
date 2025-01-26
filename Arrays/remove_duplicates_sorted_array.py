"""
Remove the duplicates from the sorted array in place

a=[1,1,2,2,3,3]

a=[1,2,3] and return the number 3

1. Brute force
 Unique elements is all about Set data structure
 Set [1,2,3]- it will not accept the duplicate elements
"""
#O(Nlogn) and space O(N)
def remove_duplicates(a):
    unique_set = set(a)  # Create a set of unique elements
    unique_list = sorted(unique_set)  # Sort the unique elements

    # Update the original array with unique elements
    for i in range(len(unique_list)):
        a[i] = unique_list[i]

    return len(unique_list)  # Return the number of unique elements

# Example usage
print(remove_duplicates([1, 1, 2, 2, 3, 3]))  # Output: 3



"""

1 2 3 2 3 3
    i     j


"""

def remove_duplicates_optimal(a):
    i=0
    for j in range(len(a)):
        if (a[j] != a[i]):
            a[i+1] = a[j]
            i+=1
    return (i+1)

print(remove_duplicates_optimal([1,1,2,2,3,3]))












#
# """
# a=[1,1,2,2,3,3]
#    l r
# output = 3
# """
#
# a=[1,2,3]

def arrCnt(arr):
    ans=0
    setArr=set(arr)
    ans=len(setArr)
    return ans

print(arrCnt([1,2,2,3,3,4,4]))















