#Date Validation
date = input("Enter a date to check whether it is valid or not: ")
day = int(date[:2])
month = int(date[3:5])
year = int(date[6:])

valyear = year>1900 and year<2022
valmonth = month>=1 and month<=12
valfebday = day>=1 and day<=29
valday = day>=1 and day<=31

if  valyear and valmonth:
    if month == 2 and valfebday:
        print("Date is valid")
    elif month != 2 and valday:
        print("Date is valid")
    else:
        print("Date is not valid")
else:
    print("Date is not valid")
