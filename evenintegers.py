numbers=input("Enter a list of integers seperated by spaces:")
num_list=[int(n) for n in numbers.split()]
odd_list=[n for n in num_list if n% 2 !=0]
print("list after removing even numbers:",odd_list)