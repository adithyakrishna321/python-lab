import calendar
year=int(input("Enter the year:"))
leap_year=calendar.isleap(year)
if leap_year:
    print("the given year is a leap year")
else:
    print("the given year is not a leap year")
