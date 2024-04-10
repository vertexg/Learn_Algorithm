def doYouFail(string):
    count = 0
    for i in string:
        if i == 'A': count += 1

        if count >= 3:
            return 'fail'
    return 'pass'
