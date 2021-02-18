import datetime, math

percent = float(input("Введите проценты по вкладу: ")) / 100
s0 = float(input("Введите начальную сумму: "))
date = datetime.date.today()
sum = 1000000

simple = (sum - s0) / (s0 * percent)
difficult = math.log(sum/s0, 1 + percent)

print("Дата открытия вклада: ", date)
print("Денег на счету: ", s0)

print("Простые проценты")
s = s0
while s < sum:
    s = s0 * percent + s
    date = date.replace(year=date.year + 1)
    print(date, '-', s)

print("\nСложные проценты")
date = datetime.date.today()
s = s0
i = 1
while s < sum:
    s = s0 * (1 + percent)**i
    date = date.replace(year=date.year + 1)
    print(date, '-', round(s, 2))
    i = i + 1
