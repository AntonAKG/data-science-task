"""
Завдання 1: Аналіз продажів
    1. Завантаж набір даних із продажами у форматі CSV (можеш створити випадкові дані).
    2. Відобрази загальну інформацію про DataFrame (розмір, типи даних, пропущені значення).
    3. Визнач місяць із найбільшими продажами.
    4. Побудуй графік зміни продажів по місяцях (line plot).
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("1task.csv")

month_order = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
data["Month"] = pd.Categorical(data["Month"], categories=month_order, ordered=True)

data = data.sort_values("Month")

max_index = data["Sales"].idxmax()
max_month = data.loc[max_index, "Month"]
max_sales = data.loc[max_index, "Sales"]

fig, ax = plt.subplots(figsize=(10, 7))
ax.plot(data["Month"], data["Sales"], marker="o", linestyle="-", color="b", label="Продажі")

ax.set_xlabel("Місяць")
ax.set_ylabel("Продажі ($)")
ax.set_title("Динаміка продажів за місяцями")
ax.grid(True)
ax.legend()

ax.annotate(f"Максимальні\n{max_month}\n{max_sales}$",
            xy=(max_month, max_sales),
            xytext=(max_month, max_sales + 1000),
            ha="center",
            arrowprops=dict(facecolor="red", shrink=0.05))

plt.xticks(rotation=45)
plt.show()
