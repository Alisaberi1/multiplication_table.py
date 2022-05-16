"""
#Write a program that prints n from the input of the multiplication table from 1 to n:

n=int(input())
for b in range (1,n+1):
    #row
    for a in range (1,n+1):
    #column
        print(b*a,end = ' ')
    print("")
"""
#or

"""
n=int(input())
for b in range (1,n+1):
    #row
    g=b
    for a in range (1,n+1):
    #column
        print(g,end = ' ')
        g+=b
    print()
    """
