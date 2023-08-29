import matplotlib.pyplot as plt

x = [2 * i / 10 for i in range(10)]
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

# Немного поэкспериментируем со стилями самих графиков
plt.plot(x, y1, label='linear',
         marker='o', linestyle='-',
         color='red', linewidth=1)
plt.plot(x, y2, label='quadratic',
         marker='v', linestyle='--',
         color='green', linewidth=1)
plt.plot(x, y3, label='cubic', marker='^',
         linestyle='-.', color='black',
         linewidth=1)

# Альтернатива: третьим аргументом передаём 
# строку с нужным форматированием цвета, линии и маркера
# plt.plot(x, y3, 'k^-.', label='cubic', linewidth=1)

plt.legend()

plt.show()