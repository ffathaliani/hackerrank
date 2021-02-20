import calendar
n1,n2,n3=map(int,input().split())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())

import calendar

m, d, y = map(int, input().split())
days = {0 : "MONDAY",
        1 : "TUESDAY",
        2 : "WEDNESDAY",
        3 : "THURSDAY",
        4 : "FRIDAY",
        5 : "SATURDAY",
        6 : "SUNDAY"}

weekday = calendar.weekday(y, m, d)
print(days[weekday])
