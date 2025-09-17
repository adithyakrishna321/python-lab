color=input("Enter comma-separated color names:")
color_list=color.split(",")
color_list=[c.strip() for c in color_list]
print("First color:",color_list[0])
print("last color:",color_list[-1])