day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
if month < 3:
    month += 12
    year -= 1
K = year % 100  
J = year // 100  
f = day + ((13*(month + 1)) // 5) + K + (K // 4) + (J // 4) - (2*J)
day_of_week = f % 7
if day_of_week == 0:
    print("Saturday")
elif day_of_week == 1:
    print("Sunday")
elif day_of_week == 2:
    print("Monday")
elif day_of_week == 3:
    print("Tuesday")
elif day_of_week == 4:
    print("Wednesday")
elif day_of_week == 5:
    print("Thursday")
elif day_of_week == 6:
    print("Friday")
print(day,month,year)
print(f,"its the anser of formula of zellers")
print(day_of_week)

