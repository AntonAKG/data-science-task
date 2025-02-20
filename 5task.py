"""
Завдання 5: Порівняння популярності соціальних мереж
    1. Створи DataFrame із даними про кількість користувачів у різних соціальних мережах за останні 5 років.
    2. Побудуй stacked bar chart, щоб показати, як змінювалась популярність платформ.
    3. Додай підписи до осей і заголовок.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Year": [2020, 2021, 2022, 2023, 2024],
    "Facebook": [2800, 2900, 2950, 3000, 3050],
    "Instagram": [1000, 1200, 1500, 1800, 2000],
    "TikTok": [500, 800, 1200, 1600, 2000],
    "Twitter": [330, 340, 350, 360, 370],
    "Snapchat": [400, 420, 450, 480, 500]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 6))

df.plot(x="Year", kind="bar", stacked=True, colormap="tab10", ax=ax)

ax.set_title("Популярність соціальних мереж за роками", fontsize=14)
ax.set_xlabel("Рік", fontsize=12)
ax.set_ylabel("Кількість користувачів (млн)", fontsize=12)

ax.legend(title="Соціальна мережа")

plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
