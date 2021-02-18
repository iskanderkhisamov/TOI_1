import math

percent = float(input("Введите проценты по вкладу: ")) / 100

sum = 1000000
s0 = 50000
simple = (sum - s0) / (s0 * percent)
difficult = math.log(sum/s0, 1 + percent)

print("Простые проценты: ", simple)
print("Сложные проценты: ", round(difficult, 2))
