'''
Array is an collection of elements, same type and they are stored in continuous block of memory
In Python, we use list to represent arrays

Operations

Access - array[index] - O(1)
Insert - array.append[value] - O(1) amortizaed
Delete - array.pop[index] - O(n) if shifting is required else O(1) on the end of the array
'''

array = [1,2,3,4,5]

print(array[1])


array.append(6)

print(array)

array.pop(2)
print(array)

'''Use only when we need ordered data or frequent index based access]
Ideal for the collections where order matters
'''