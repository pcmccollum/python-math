def factors(num):
    factorsList = []
    for i in range(1, num+1):
        if num % i == 0:
            factorsList.append(i)
    return factorsList


def gcf(num1, num2):
    factorsList1, factorsList2 = [], []
    factorsList1 = factors(num1)
    factorsList2 = factors(num2)
    commonFactor = 0
    for i in factorsList2:
        for j in factorsList1:
            if i == j:
                commonFactor = i
    return commonFactor


print(gcf(256, 1024))
