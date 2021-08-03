def average(numList):
    return sum(numList) / len(numList)


def mySum(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i
    return running_sum


print(average([53, 28, 54, 84, 65, 60, 22, 93, 62, 27,
      16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]))

print(f'100 sum: {mySum(100)}')
print(f'1000 sum: {mySum(1000)}')
