def tennis_ball(num):
    i = 1
    while i < 6:
        if num % 3 == 0:
            num = num / 3
        elif num % 2 != 0:
            num = num * 4
            num = num + 2
        else:
            num = num + 1
        i = i + 1
    return num
