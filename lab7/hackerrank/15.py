# https://www.hackerrank.com/challenges/calendar-module/problem
import calendar


def findDay(date):
    month, day, year = (int(i) for i in date.split(' '))
    dayNumber = calendar.weekday(year, month, day)
    days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY",
            "FRIDAY", "SATURDAY", "SUNDAY"]
    return (days[dayNumber])


date = input()
print(findDay(date))
