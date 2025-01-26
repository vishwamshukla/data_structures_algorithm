"""
Check if the array is sorted or not

a =[1,2,2,3,3,4] it is sorted
a=[1,2,1,3,4] it is not sorted

"""

def check_array_sorted(a): #Time = O(N)
    for i in range(1, len(a)):
        if (a[i] >= a[i-1]):
            pass
        else:
            return False
    return True

print(check_array_sorted([1,2,2,3,7,4]))