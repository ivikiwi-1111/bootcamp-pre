'''
Попробуем всё немного усложнить
'''
import matplotlib.pyplot as plt

# Зададим X
x = [2 * i / 100 for i in range(100)] 
# Эта штука называется list comprehension.
# Позволяет удобно создавать list'ы.
# Но нам такой способ понадобится только в этом примере.
# Далее будет предложена ещё более удобная альтернатива.
# Данная строчка эквивалентна такому коду:
x = []
for i in range(100):
    x.append(2 * i / 100)



# А это три штуки y(x)
y1 = [i for i in x]
y2 = [i**2 for i in x]
y3 = [i**3 for i in x]

# Построим графики, указав названия
plt.plot(x, y1, label='linear')
plt.plot(x, y2, label='quadratic')
plt.plot(x, y3, label='cubic')

# Подпишем оси
plt.xlabel('x label')
plt.ylabel('y label')
# И график целиком
plt.title("Simple Plot")
# И легенду нарисуем, чтобы было ясно, кто есть кто
plt.legend()

plt.show()



