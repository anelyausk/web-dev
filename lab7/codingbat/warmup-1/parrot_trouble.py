def parrot_trouble(talking, hour):
    if talking == True and (20 < hour or hour < 7):
        return True
    return False


parrot_trouble(True, 6)
