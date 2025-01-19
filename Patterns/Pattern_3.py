'''
1
12
123
1234
12345

for outer loop i till 5
for inner loop j till i+1
'''

def printPattern3(n):
    for i in range(n):
        for j in range(1, i+2):
            print(j, end='')
        print()

printPattern3(5)

def printPattern4(n):
    for i in range(n):
        for j in range(1, i+2):
            print(i+1, end='')
        print()

printPattern4(5)