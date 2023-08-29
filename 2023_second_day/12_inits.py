"""
Посмотрим на различные способы создания массивов
"""
import numpy as np

# Аналогично встроенному range:
# двигаемся от -5 до 15 с шагом 2, не включая правый край
print("arange:", np.arange(-5, 15, 2))

# Хотим массив два на два из случайных чисел
print("random: \n", np.random.random((2, 2)))

# Хотим массив длиной 3 из единиц
print("ones:", np.ones(3))

# Массив из нулей длиной 10
print("zeros:", np.zeros(10))

# Массив из 10 элементов, заполненный значением 42.0
print("full:", np.full(10, 42.0))

# Массив со значениями от 0 до 2 включительно с 5-ю
# элементами и равными промежутками между числами
print("linspace:", np.linspace(0, 2, 5))
# x = np.linspace(0, 2, 100)
