import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию f(z)
def f(z):
    return z ** 5 - 1

# Определяем её производную f'(z)
def df(z):
    return 5 * z ** 4

# Метод Ньютона для нахождения корней
def newton_method(z, max_iter=100):
    for _ in range(max_iter):
        z -= f(z) / df(z)
    return z

# Создаем сетку комплексных чисел
def create_fractal(xmin, xmax, ymin, ymax, width, height):
    # Создаем массивы значений для действительной и мнимой частей комплексных чисел
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    # Создаем сетку из координат (действительная и мнимая части)
    Z = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
    # Преобразуем двумерные координаты в одномерный массив комплексных чисел
    Z = Z[:, 0] + 1j * Z[:, 1]

    # Применяем метод Ньютона
    # Применяем метод Ньютона к каждому элементу массива Z, получая массив корней
    roots = np.array([newton_method(z) for z in Z])

    # Получаем цвет по корням
    # Определяем цвет для каждой точки на основе того, к какому корню она сошлась
    colors = np.angle(roots) / (2 * np.pi)
    # Возвращаем массив цветов в форме двумерного массива с размерами height x width
    return colors.reshape(height, width)

#  Устанавливаем границы области отображения и размеры изображения
xmin, xmax = -2, 2
ymin, ymax = -2, 2
width, height = 800, 800

# Создаем фрактал
# Получаем цветовые значения для каждого пикселя
fractal_colors = create_fractal(xmin, xmax, ymin, ymax, width, height)

# Визуализация
# plt.imshow(...) Отображает массив цветов как изображение
# Параметр extent задает границы отображаемой области
# cmap='Set3' Указывает цветовую карту для визуализации
plt.imshow(fractal_colors, extent=(xmin, xmax, ymin, ymax), cmap='Set3')

# Добавляем цветовую шкалу к изображению
plt.colorbar()
# Устанавливаем заголовок и подписи осей
plt.title('Фрактал для f(z) = z^5 - 1')
plt.xlabel('Re(z)')
plt.ylabel('Im(z)')
plt.show()
