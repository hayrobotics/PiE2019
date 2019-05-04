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

def gets_coins(num):
    total = 0
    quarters = 0
    nickels = 0
    pennies = 0
    while total < num:
        if not total + 25 > num:
            total += 25
            quarters += 1
        else:
            if not total + 5 > num:
                total += 5
                nickels += 1
            else:
                if not total + 1 > num:
                    total += 1
                    pennies += 1

    return int(str(quarters) + str(nickels) + str(pennies))

# Still in Progress

def most_common(num):
  frequency = {}
  for digit in list(str(num)):
    if digit in frequency.keys():
      frequency[digit] += 1
    else:
      frequency[digit] = 1
  
  # We almost wrote this: return int(list(frequency.keys())[list(frequency.values()).index(max(list(frequency.values())))]
  keys = list(frequency.keys())
  values = list(frequency.values())
  
  most_common = keys[(values.index(max(values)))]

  return int(most_common)
