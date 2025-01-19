'''
*
**
***
****
*****

outer for loop for 5
inner loop runs for when i=0 j-0, i=1, j=1, i=2, j = 2 I mean when j<=i for every i
'''

def printPattern(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()

printPattern(5)