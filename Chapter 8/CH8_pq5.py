#Write a python function to print first n lines of the following pattern.sum
'''
***
**
*  for n = 3
'''

def pat(n):
    if n==0:
        return
    print("*"*n)
    pat(n-1)


pat(5)