'''
1. For the outer loop, count the number of lines
2. For the inner loop, focus on the column and connect them witht he rows
3. Print them with "*" inside the inner loop
4. Observe Symmetry [optional]
'''

'''
****
****
****
****
'''

'''
Outer for loop for 4 times -  i to 4
Inner for loop for 4 times as well - j to 4
'''

def printPattern(n):
    for i in range(n):
        for j in range(n):
            print("* ", end="")
        print()

printPattern(4)