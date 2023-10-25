# This is a program that checks whether a year is a leap year or not


year = int(input('2019:'))
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 100) == 0:
            print('is a leap year')
        else:
            print('is not a leap year')
    else:
        print('is a leap year')
else:
    print('is not a leap year')
