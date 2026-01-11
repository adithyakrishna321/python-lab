a=input("Enter a string:")
if len(a)>1:
    print(a[-1]+a[1:-1]+a[0])
else:
    print(a)