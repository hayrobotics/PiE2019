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

def remove_duplicates(num):
    num = str(num)
    numlist = list(dict.fromkeys(list(num)))
    newnum = int("".join(numlist))
    return newnum

def rotate(num):
    i = 0
    num = str(num)
    numlist = list(num)
    while i < max(map(int, numlist)):
        tbi = numlist[len(numlist) - 1]
        numlist.pop(len(numlist) - 1)
        numlist.insert(0, tbi)
        i = i + 1
    newnum = int("".join(numlist))
    return newnum

def next_fib(num):
    first, second, third = 0, 1, 1
    if num == 0:
        return 0
    else:
        while num > third:
            first = second
            second = third
            third = first + second
        return third

# Still in Progress

def most_common(num):
    i, final, newlist = 0, "", []
    num = str(num)
    numlist = list(num)
    count = {}
    for x in numlist:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    while i < 4:
        newlist.append(max(count))
        count.pop(max(count))
        i = i + 1
    i = 0
    newlist = list(map(int, newlist))
    while i < 4:
        final = final + str(max(newlist))
        newlist.remove(max(newlist))
        i = i + 1
    final = int(final)
    print(final)

most_common(12345)