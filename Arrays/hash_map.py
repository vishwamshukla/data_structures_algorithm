'''
A hashmap or dictonary in python is a data structure that maps the key to values for efficient data retrieval

Operations

Insert - dict[key] = value   - O(1)
Access - dict[key]   - O(1)
Delete - del dict[key]    -  O(1)
'''

hashmap = {"a":1, "b":2, "c":3}

print(hashmap["a"])

hashmap["d"] = 4
print(hashmap)

del hashmap["d"]
print(hashmap)



'''Use for fast look up, insertion, deletion by key
Ideal when you need mapping betweeen key and value
'''