start_range=int(input("Enter the starting range (4 digit min):"))
end_range=int(input("Enter the ending range (4 digit max):"))
evendigit=[]
for num in(start_range,end_range + 1):
    sqrt=int(num ** 0.5)
    if sqrt * sqrt == num:
        evendigit.append(num)
        if evendigit !=[]:
            print("Numbers with all even digits and are perfect squares:")
            print(evendigit)
        else:
            print("There are no numbers the given range.")
