def sleep_in(weekday, vacation):
    if weekday == False and vacation == False:
        return True
    elif weekday == True and vacation == False:
        return False
    elif weekday == False and vacation == True:
        return True
    elif weekday == True and vacation == True:
        return True


weekday = True
vacation = False
sleep_in(weekday, vacation)
