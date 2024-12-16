import plotly.express as px
import seaborn as sns
import numpy as np
import pandas as pd

# загружаем датасет чаевых (tips dataset)
# этот набор имеет данные : total_bill, tip, sex, smoker, day, time, size
df = tips = px.data.tips()

'''
Plotly      базовый вывод: линейный график (line plot) по дням (x) и средний общий счет (y)
'''

# считаем pandas данные: группируем по дням и считаем средний чек
df_grouped = df.groupby('day')['total_bill'].mean().reset_index()
fig = px.line(df_grouped, x="day", y="total_bill", title="Plotly. Линейный график: средний общий счет за день")
fig.show()

'''
Plotly      базовый вывод: круговая диаграмма (pie chart).
            Общее распределение счетов по дням.
'''

fig = px.histogram(df, x="total_bill", facet_row="day", facet_col="time",
                   nbins=30, title="Общее распределение счетов по дням")
fig = px.pie(df, names='day', values='total_bill', title="Plotly. Общее распределение счетов по дням")
fig.show()

'''
Plotly      коробчатый график (box plot) общего счета в разбивке по дням и полу.
'''

fig = px.box(df, x="day", y="total_bill", color="sex", title="Plotly. Коробчатый график "
                                                             "общего счета в разбивке по дням и полу")
fig.show()

'''
Plotly      диаграмма рассеяния (scatter plot) показывающая соотношение чаевых 
            и общего счета в зависимости от статуса (не)курильщика.
'''

fig = px.scatter(df, x="total_bill", y="tip", color="smoker", size='size', opacity=0.3,
                 title="Plotly. Соотношение чаевых и общего счета в зависимости от статуса (не)курильщика")
fig.show()

'''
Plotly      диаграмма общего счета (sunburst chart) в разбивке по дням, полу и времени  
'''

fig = px.sunburst(df,
                  path=['day', 'sex', 'time'],  # фильтры по выводу диаграмм
                  values='total_bill',
                  title="Plotly. Подробная круговая диаграмма общего счета в разбивке по дням, полу и времени")
fig.show()

'''
Plotly      трехмерная диаграмма рассеяния (3D scatter plot)
            эффектный 3D график, показывающий зависимость чаевых (tip) от
            общей суммы счета(total bill), разбитый по 
            времени (выделено разной формой и цветом) и размеру компании
'''

fig = px.scatter_3d(df,
                    x='total_bill',
                    y='tip',
                    z='size',
                    color='day',
                    symbol='time',
                    size='size',
                    opacity=0.5,
                    title="Plotly. 3D график зависимости чаевых(tip) от общей суммы счета(total bill): "
                          "по дням, времени и размеру компании(party size)")

fig.update_layout(scene=dict(  # обновленный макет осей X,Y,Z для сцены
    xaxis_title='Total Bill',
    yaxis_title='Tip',
    zaxis_title='Party Size'
))
fig.show()

'''
Plotly      пример использования карты хороплет (choropleth map),
            натягиваем датасет с чаевыми на глобус (на фоновую картограму)
'''

df = px.data.tips()

# симулируем данные
location_map = {'Thur': 'RUS', 'Fri': 'DEU', 'Sat': 'CHN', 'Sun': 'USA'}
df['location'] = df['day'].map(location_map)

# подсчитываем сумму чека в зависимости от местоположения
location_data = df.groupby('location')['total_bill'].sum().reset_index()

# Создаем  карту хороплета (choropleth map)
fig = px.choropleth(location_data, locations='location', color='total_bill',
                    hover_name='total_bill', projection='natural earth',
                    title='Plotly. Общий счет по местоположению', color_continuous_scale='Sunsetdark')
fig.show()
