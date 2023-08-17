#Write a Python program that accepts a word from the user and reverse it.
'''
Note:
Sample Test Case
Input : Edyoda
output: adoydE   
'''

str1 = input("Hello!! please enter the text: ")
reversed_string = ""
for i in range(len(str1)-1,-1,-1):
    reversed_string += str1[i]
print("your reversed text is :", reversed_string )