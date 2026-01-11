list1=input("Enter color for list 1 (Comma seperated: ").split(",")
list2=input("Enter color for list 2 (Comma seperated: ").split(",")
for color in list1:
    if color not in list2:
        print(color)