summ = 0
while (price := float(input())) != 0:
    if price < 500:
        summ += price
    else:
        summ += 0.9 * price
print(summ)