num=int(input("enter the number for multiplication table:"))
i=1
print(f"factors of (num) are:")
while i<=num:
    if num%i==0:
        print(i,end="")
        i+=1

