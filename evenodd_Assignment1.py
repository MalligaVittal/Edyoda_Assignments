# Write a Python program to count the number of even and odd numbers from a series of numbers.
'''
Note:
Sample numbers : numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
Expected Output :
Number of even numbers : 4
Number of odd numbers : 5
'''

start_value = int(input("Enter the start value: "))
end_value = int(input("Enter the start value: "))
even_num = 0
odd_num = 0
for i in range (start_value, end_value):
    if (i % 2 == 0):
        even_num += 1
    else:
        odd_num += 1
print("Number of even numbers : ", even_num)
print("Number of odd numbers : ", odd_num)
