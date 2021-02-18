import datetime
import math
import matplotlib.pyplot as plt
import numpy as np

percent = float(input("Введите проценты по вкладу: ")) / 100
s0 = float(input("Введите начальную сумму: "))
date = datetime.date.today()
sum = 1000000

simple = (sum - s0) / (s0 * percent)
difficult = math.log(sum/s0, 1 + percent)

print("Дата открытия вклада: ", date)
print("Денег на счету: ", s0)

simple_dates = []
simple_sums = []

print("\nПростые проценты")
s = s0
simple_sums.append(s)
simple_dates.append(date)
while s < sum:
    s = s0 * percent + s
    simple_sums.append(round(s))
    date = date.replace(year=date.year + 1)
    simple_dates.append(date)
    print(date, '-', s)

difficult_dates = []
difficult_sums = []

print("\nСложные проценты")
date = datetime.date.today()
s = s0
i = 1
difficult_sums.append(s)
difficult_dates.append(date)
while s < sum:
    s = s0 * (1 + percent)**i
    difficult_sums.append(round(s))
    date = date.replace(year=date.year + 1)
    difficult_dates.append(date)
    print(date, '-', round(s, 2))
    i = i + 1

fig, ax = plt.subplots()
ax.plot(simple_dates, simple_sums, label='Простые проценты')
ax.plot(difficult_dates, difficult_sums, label='Сложные проценты')
ax.legend(fontsize=14, ncol=1)
plt.xlabel("Дата")
plt.ylabel("Сумма денег")
plt.show()
