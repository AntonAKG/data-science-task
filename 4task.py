"""
Завдання 4: Аналіз трафіку на сайті
    1. Створи DataFrame, що містить дані про кількість відвідувачів сайту за кожен день протягом 3 місяців.
    2. Визнач дні з найбільшою та найменшою активністю.
    3. Побудуй гістограму (histogram), що показує розподіл кількості відвідувачів.
    4. Додай вертикальну лінію на гістограму, що позначає середнє значення.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start="2024-01-01", periods=90, freq="D")
visitors = np.random.randint(500, 5000, len(dates))
df_traffic = pd.DataFrame({"Date": dates, "Visitors": visitors})

max_day = df_traffic.loc[df_traffic['Visitors'].idxmax()]
min_day = df_traffic.loc[df_traffic['Visitors'].idxmin()]

fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(df_traffic['Visitors'], bins=15, color='skyblue', edgecolor='black', alpha=0.75)

mean_value = df_traffic['Visitors'].mean()
ax.axvline(mean_value, color='red', linestyle='dashed', linewidth=2, label=f'Середнє: {mean_value:.1f}')

ax.set_title("Розподіл кількості відвідувачів на сайті", fontsize=14)
ax.set_xlabel("Кількість відвідувачів", fontsize=12)
ax.set_ylabel("Частота", fontsize=12)
ax.legend()

plt.show()
