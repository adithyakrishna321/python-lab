from math import factorial

num=int(input("Enter a number: "))
factorial=1
for i in range(1,num+1):
    factorial*=i
print("the factorial of",num,"is",factorial)
