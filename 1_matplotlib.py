import matplotlib.pyplot as plt  # функции для построения графиков
import numpy as np  # работы с массивами данных и выполнения математических операций
import pandas as pd
from matplotlib.widgets import Slider  # для интерактивных ползунков
from mpl_toolkits.mplot3d import Axes3D

'''
MatPlotLib:     базовый линейный график (line plot)

'''

# x=[1,2,3,4,5]       # значения x можно задать как списком
# x=(1,2,3,4,5)       # так и кортежем
# x=range(1,5,1)      # можно используем встроенную функцию для генерации (но только int)
# x = pd.DataFrame({'Value': [1,2,3,4,5]})  # так и pandas dataframe

# наиболее корректный вариант: создаем последовательность данных с помощью библиотеки numpy
# расположенных на числовой прямой в заданном интервале и с заданным промежутком
x = np.linspace(-20, 20, 100)
y = x * np.sin(x)

plt.figure(figsize=(10, 6))  # задаем холст, размеры

# colors and style https://matplotlib-cpp.readthedocs.io/en/latest/style.html
plt.plot(x, y, label='x * sin(x)', color='tab:olive', linestyle='-', linewidth=2, marker='o', markersize=3)
plt.title('MatPlotLib. Линейный график — Line plot', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=11)
plt.ylabel('x * sin(x)', fontsize=11)
plt.legend(fontsize=11)
plt.grid(True, linestyle='--', alpha=0.3)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)
# plt.tight_layout() # сжимает холст, бывает полезно #plt.minorticks_on()
plt.savefig('1matplotlib_1line_plot.png')
plt.show()
plt.close()

'''
MatPlotLib:     Диаграмма рассеяния - Scatter plot

'''

# генерируем случайные данные для графика
x = np.random.rand(50)
y = np.log(np.random.rand(50))
colors = np.random.rand(50)
sizes = 1000 * np.random.rand(50)

plt.figure(figsize=(10, 6))
# colormaps : matplotlib.org/stable/users/explain/colors/colormaps.html
scatter = plt.scatter(x, y, c=colors, s=sizes, alpha=0.4, cmap='copper', edgecolor='w', linewidth=0.5)
plt.title('MatPlotLib. Диаграмма рассеяния (scatter plot)', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.colorbar(scatter, label='Color scale', orientation='vertical', pad=0.02)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tick_params(axis='both', which='major', labelsize=12)
plt.tick_params(axis='both', which='minor', labelsize=10)
plt.savefig('1matplotlib_2scatter_plot.png')
plt.show()
plt.close()

'''
MatPlotLib:     Столбчатая диаграмма / Bar Chart

'''

categories = ['А', 'Б', 'В', 'Г']
values = [10, 15, 7, 10]

plt.figure(figsize=(8, 4))
plt.bar(categories, values, color=['blue', 'skyblue', 'purple', 'tab:purple'])
plt.title('MatPlotLib. Столбчатая диаграмма (bar chart)', fontsize=12, fontweight='normal')
plt.xlabel('Категории')
plt.ylabel('Значения Y')
plt.savefig('1matplotlib_3bar_chart.png')
plt.show()
plt.close()

'''
MatPlotLib:     Гистограмма (histogram)

'''

data = np.sin(np.random.randn(1000))
plt.figure(figsize=(8, 4))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('MatPlotLib. Гистограмма (histogram)')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.savefig('1matplotlib_4histogram.png')
plt.show()
plt.close()

'''
MatPlotLib:     на одном холсте можно выводить несколько графиков

'''

# Создаем данные для линейного графика
x_line = np.linspace(-10, 10, 100)
y_line = x_line * np.sin(x_line)

# Создаем данные для гистограммы
data_hist = np.random.randn(100) ** ((y_line) != 0)

# Создаем фигуру и оси с двумя подграфиками
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Линейный график слева
ax1.plot(x_line, y_line, label='Линейный график', color='tab:red', linestyle='-', linewidth=2, marker='o', markersize=3)
ax1.set_title('Линейный график', fontsize=16)
ax1.set_xlabel('x', fontsize=14)
ax1.set_ylabel('  x*sin(x) ', fontsize=14)
ax1.legend(fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
# ax1.minorticks_on()
ax1.tick_params(axis='both', which='major', labelsize=12)
ax1.tick_params(axis='both', which='minor', labelsize=10)

# Гистограмма справа
ax2.hist(data_hist, bins=30, color='tab:red', edgecolor='k', linewidth=0.5, alpha=0.7)
ax2.set_title('Гистограмма', fontsize=14)
ax2.set_xlabel('Значения', fontsize=12)
ax2.set_ylabel('Частота', fontsize=12)
ax2.grid(axis='y', linestyle='--', alpha=0.7)
# ax2.minorticks_on()
ax2.tick_params(axis='both', which='major', labelsize=12)
ax2.tick_params(axis='both', which='minor', labelsize=10)

# Добавляем общее название для всего холста
fig.suptitle('MatPlotLib. Два графика на одном холсте', fontsize=16, fontweight='bold')
plt.savefig('1matplotlib_5two_plots.png')
plt.show()
plt.close()

'''
MatPlotLib:     3D график 

'''

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Генерируем случайные данные
np.random.seed(0)  # Для воспроизводимости результатов
x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)

# Генерируем значения для цвета
color_ = np.sqrt(x ** 2 + y ** 2 + z ** 2)

# Настройки для маркеров
marker_size = 50
marker_alpha = 0.6

# Построение данных
scatter = ax.scatter(x, y, z, c=color_, cmap='viridis', s=marker_size, alpha=marker_alpha, edgecolor='w', linewidth=0.5)

# Добавляем цветовую панель
cbar = fig.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)
cbar.set_label('Расстояние от центра')

# Устанавливаем метки осей
ax.set_xlabel('ось X', fontsize=10)
ax.set_ylabel('ось Y', fontsize=10)
ax.set_zlabel('ось Z', fontsize=10)

# Устанавливаем заголовок
ax.set_title('MatPlotLib: 3D диаграмма рассеяния (3D Scatter Plot) с цветными маркерами', fontsize=14)
ax.grid(True)  # Добавляем сетку

plt.savefig('1matplotlib_6_3d_plots.png')
plt.show()
plt.close()

'''
MatPlotLib:     Интерактивные графики (interactive plots)

'''


# from matplotlib.widgets import Slider   # для интерактивных ползунков импортируем класс Slider

# функция синусоидальной волны
def sine_wave(x, freq, amp):
    return amp * np.sin(freq * x)


# создаем данные для волны
x = np.linspace(0, 2 * np.pi, 100)
y = sine_wave(x, 1, 1)  # 1, 1 первоначальные значения частоты и амплитуды

# делаем фигуру и ось
fig, ax = plt.subplots()
line, = ax.plot(x, y, lw=2)
ax.set_xlabel('x')
ax.set_ylabel('Амплитуда')
ax.set_title('MatPlotLib. Интерактивная синусоидальная волна')

# место для ползунков
fig.subplots_adjust(left=0.3, bottom=0.3)  # отступы от осей

# горизонтальный ползунок для управления частотой
axfreq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Частота [Hz]',
    valmin=0.1,
    valmax=10.0,
    valinit=1,
)

# вертикально ориентированный ползунок для управления амплитудой
axamp = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
amp_slider = Slider(
    ax=axamp,
    label="Амплитуда",
    valmin=0.1,
    valmax=2.0,
    valinit=1,
    orientation="vertical"
)


# Функция, вызывающаяся при каждом изменении значения ползунка
def update(val):
    line.set_ydata(sine_wave(x, freq_slider.val, amp_slider.val))
    fig.canvas.draw_idle()


# функция для обновления при изменении каждого ползунка
freq_slider.on_changed(update)
amp_slider.on_changed(update)

plt.show()
plt.close()
