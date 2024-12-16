import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import mplcursors

'''
Seaborn     имеет более 20 наборов данных, здесь для примеров визуализации будет использован датасет "tips",
            который содержит информацию о чаевых, оставленных в ресторане. Описание каждого столбца: 
            total_bill: общая сумма счета (в долларах).
            tip: сумма чаевых (в долларах).
            sex: пол клиента (male/female).
            smoker: курит ли клиент (yes/no).
            day: день недели (thur/sat/sun/fri)
            time: время дня (lunch/dinner).
            size: количество людей в группе.
'''

tips = sns.load_dataset("tips")  # загрузка датасета "tips"
# print(tips.head(3))                 # просмотр первых 3 строк
# print(tips.info())                  # информация о датасете
# print(tips.describe())              # статистические показатели


'''
Seaborn:    Высокоуровневая библиотека, на основе Matplotlib. 
            Seaborn абстрагирует многие из деталей позволяя создавать сложные визуализации с меньшим количеством кода.

            Seaborn и Matplotlib сравнение на примере базового графика функции sin 
'''

# Пример на Matplotlib
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='sin(x)', color='blue', linestyle='-', linewidth=2)
plt.title('Seaborn. Синусоидальная волна')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
plt.close()

# Аналогичный пример на Seaborn
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.figure(figsize=(8, 6))

# Функция sns.set() позволяет установить глобальные настройки стиля, включая размеры шрифтов,
# стили осей и другие параметры. Однако она не размеры отступов и холста напрямую
sns.set(style="whitegrid")
sns.lineplot(x=x, y=y, label='sin(x)', color='blue')
plt.title('Seaborn. Синусоидальная волна')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.show()
plt.close()

'''
Seaborn     Встроенная статистическая визуализация, в Matplotlib это либо недоступно, либо требуют весомых усилий 
            Регрессионные графики: позволяют визуализировать линейную регрессию
'''

sns.set(style="whitegrid", font_scale=1)
sns.regplot(x="total_bill", y="tip", data=tips)  # Построение линейной регрессии между суммой и чаевыми
plt.title('Seaborn. Линейная регрессия: сумма чека vs сумма чаевых')  # Добавление заголовка и меток осей
plt.xlabel('Сумма чека')
plt.ylabel('Сумма чаевых')
plt.savefig('2_seaborn_1_regplot.png')
plt.show()
plt.close()

'''
Seaborn     Графики распределения упрощают визуализацию распределений с опциями для оценки 
            плотности ядра (KDE) и эмпирической функции распределения
    
            Гистограмма с разделением по категориальной переменной с разными цветами
'''

# Построение гистограммы с разделением по переменной 'sex' с разными цветами, с указанием пределов оси X и
sns.histplot(tips, x="total_bill", hue="sex", multiple="dodge", bins=15, palette="pastel", binrange=(0, 50))

plt.title('Seaborn. Гистограмма суммы чека и разделение по полу с разными цветами')
plt.xlabel('Сумма чека')
plt.ylabel('Частота')
plt.savefig('2_seaborn_2_histplot.png')
plt.show()
plt.close()

'''
Seaborn     Реляционные графики: Функции, такие как sns.relplot(), позволяют легко визуализировать 
            взаимосвязи между переменными с поддержкой группировки по дополнительным измерениям (цвет, размер, стиль)

            Построение точечного графика с разделением по переменной 'sex'
'''

# Многие функции Seaborn: relplot(), catplot(), displot(), имеют height и aspect, что позволяет задавать размеры графика
sns.relplot(x="total_bill", y="tip", hue="sex", data=tips, height=6, aspect=1.5)
plt.title('Seaborn. Точечный график: сумма чека vs сумма чаевых и разделение по полу')
plt.xlabel('Сумма чека')
plt.ylabel('Сумма чаевых')

# Настройка отступов между подграфиками и между границами графика и окном
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.savefig('2_seaborn_3_relplot.png')
plt.show()
plt.close()

'''
Seaborn     многопанельных многофункциональные гриды для создания нескольких сеток, 
            которые упрощают создание сложных визуализаций из нескольких сеток,
            что потребовало бы значительных усилий в Matplotlib

            FacetGrid: Сетка для построения условных отношений.
'''

grid = sns.FacetGrid(tips, col="time", row="sex", margin_titles=True)
grid.map(sns.histplot, "total_bill", bins=15, color="purple")
plt.savefig('2_seaborn_4_grid.png')
plt.show()
plt.close()

'''
Seaborn     swarmplot() используется для создания точечных графиков, где точки размещаются таким образом, 
            чтобы избежать наложения когда нужно показать распределение непрерывных переменных внутри каждой категории,
            что недоступно непосредственно в Matplotlib.
'''

plt.figure(figsize=(10, 5))  # Создание фигуры с заданными размерами

# Построение swarm plot с разделением по переменной 'sex'
sns.swarmplot(x="day", y="tip", hue="sex", data=tips, dodge=True, palette="Set2", size=5, alpha=0.75)
plt.subplots_adjust(left=0.15, right=0.9, top=0.9, bottom=0.15)  # Настройка отступов
plt.title('Seaborn. Swarm plot: Сумма чаевых по дням недели и разделение по полу')
plt.xlabel('День недели')
plt.ylabel('Сумма чаевых')
plt.savefig('2_seaborn_5_swarmplot.png')
plt.show()
plt.close()

# Создание сводной таблицы
pivot_table = tips.pivot_table(index="day", columns="time", values="total_bill", aggfunc="mean", observed=False)

# Построение тепловой карты сводной таблицы
sns.heatmap(pivot_table, annot=True, cmap="viridis", fmt=".1f", linewidths=0.5)  # cmap="YlGnBu"
plt.title('Seaborn. Тепловая карта средних сумм чека по дням и времени')
plt.savefig('2_seaborn_6_heatmap.png')
plt.show()
plt.close()

'''
Seaborn:    3D график получили на 22 строках
MatPlotLib  аналогичный 3D график на 36 строках
'''

sns.set(style="whitegrid")

np.random.seed(0)
x = np.random.standard_normal(100)
y = np.random.standard_normal(100)
z = np.random.standard_normal(100)

# Создание 3D дисперсного графика
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', marker='o')

# Добавление подписей осей
plt.title('Seaborn. 3D диаграмма рассеяния (3D Scatter Plot) с цветными маркерами', fontsize=14)
ax.set_xlabel('X Ось')
ax.set_ylabel('Y Ось')
ax.set_zlabel('Z Ось')

# Добавление цветовой шкалы, которая отображает значения цветами
plt.colorbar(scatter, ax=ax, shrink=0.5, aspect=5)
plt.savefig('2_seaborn_7_heatmap.png')
plt.show()
plt.close()

'''
Seaborn:    интерактивная диаграмма рассеяния (scatter plot)
            при наведении курсора показываются дополнительные данные
'''

plt.figure(figsize=(12, 8))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', palette='viridis',
                alpha=0.4, size='size', sizes=(10, 400))  # если s=50 то размер всех точек на графике будет 50


def on_select(sel):
    sel.annotation.set(
        text=(
            f"общий счет: ${sel.target[0]:.1f}\n"
            f"чаевые: ${sel.target[1]:.1f}\n"
            f"день: {tips.iloc[sel.index]['day']}\n"
            f"время: {tips.iloc[sel.index]['time']}\n"
            f"пол: {tips.iloc[sel.index]['sex']}\n"
            f"людей в группе: {tips.iloc[sel.index]['size']}"
        )
    )


mplcursors.cursor(hover=True).connect("add", on_select)

plt.title("Seaborn. Интерактивная диаграмма рассеяния для набора данных Tips")
plt.xlabel("Общий счет ($)")
plt.ylabel("Чаевые ($)")
plt.legend()
plt.savefig('2_seaborn_8_interact.png')
plt.show()

'''
Seaborn     функции Seaborn "ориентированы на данные", т.е. они понимают структуру вашего набора данных 
            и могут автоматически извлекать метки осей, легенды и другие элементы графика. 
            В Matplotlib эти элементы необходимо явно определять.
            Встроенная поддержка доверительных интервалов автоматически рассчитывается и 
            отображаются доверительные интервалы для многих типов графиков,
            например, регрессионных линий, линейных графиков, столбчатых графиков, 
            что в Matplotlib потребовало бы ручного расчета и построения. 
            
Matplotlib  производительность обычно быстрее для простых графиков из-за своего низкоуровневого характера.
            Seaborn может быть медленнее для больших наборов данных из-за своих высокоуровневых 
            абстракций и дополнительных вычислений.
'''
