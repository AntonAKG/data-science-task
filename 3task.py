"""
Завдання 3: Дослідження погоди
    1. Завантаж набір даних про температуру за рік.
    2. Визнач середню температуру по місяцях.
    3. Побудуй графік (scatter plot або line plot), що показує зміну температури по місяцях.
    4. Додай трендову лінію до графіка.
"""

import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv("3task.csv")

avarage = data['Temperature'].mean()

fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(data['Month'], data['Temperature'], color='b', label='Температура', marker='o', linestyle='-')

ax.set_title('Зміна температури по місяцях')
ax.set_xlabel('Місяць')
ax.set_ylabel('Температура')
ax.annotate(f'Середня температура\n{avarage:.1f}°C', xy=(6, avarage), xytext=(6, avarage + 1), ha='center',
            arrowprops=dict(facecolor='red', shrink=0.05))
ax.legend()
ax.grid(True)


plt.xticks(rotation=45)
plt.show()
