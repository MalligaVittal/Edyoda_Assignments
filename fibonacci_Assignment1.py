# Write a Python program to get the Fibonacci series between 0 to 50
'''
Note : The Fibonacci Sequence is the series of numbers :
0, 1, 1, 2, 3, 5, 8, 13, 21, ....
Every next number is found by adding up the two numbers before it.
Expected Output : 1 1 2 3 5 8 13 21 34
'''

# start= int(input("Enter the range in number :  "))
# num1 = 0
# num2 = 1
# #print("Fibonacci series:", num1, num2, end= " ")
# for i in range(2, start):
#     if i<=1:
#         next= i
#     else:
#         next= num1+num2
#         num1= num2
#         num2= next
#         print(next)


number= int(input("Enter the range in number :  "))
def fib(number):
    count =0
    first=1
    second=1
    temp=0
    while count<=number:
        print(first)
        temp=first+second
        first=second
        second=temp
        count=count+1
fib(number) 

    

