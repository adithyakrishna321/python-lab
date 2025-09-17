numbers=input("Enter a list of integers seperated by spaces:")
num_list=[int(n) for n in numbers.split()]
greater_than_100=[n for n in num_list if n> 100]
print("Numbers greater than 100 are:",greater_than_100)