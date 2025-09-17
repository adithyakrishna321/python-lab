color_list1=input("Enter color for list 1(coma seperated: )").split(',')
print(color_list1)
color_list2=input("Enter color for list 2(coma seperated: )").split(',')
print(color_list2)
unique_color=[color for color in color_list1 if color not in color_list2]
print("colors from colorlist one not in list 2:")
print(unique_color)
