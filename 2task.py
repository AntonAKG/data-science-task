import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Генерація випадкових даних
data = {
    "Student": ["Олег", "Марія", "Іван", "Анна", "Сергій", "Катерина"],
    "Math": np.random.randint(40, 100, 6),
    "Physics": np.random.randint(40, 100, 6),
    "English": np.random.randint(40, 100, 6),
    "Attendance (%)": np.random.randint(60, 100, 6),
}

df_students = pd.DataFrame(data)

# Обчислення середнього балу
df_students["Average"] = df_students[["Math", "Physics", "English"]].mean(axis=1)



# Визначення студентів із низьким балом (<50)
failed_students = df_students[df_students["Average"] < 50]
print("Студенти з середнім балом нижче 50%:\n", failed_students[["Student", "Average"]])

# Візуалізація даних
fig, ax = plt.subplots(figsize=(10, 7))

colors = ["red" if avg < 50 else "green" for avg in df_students["Average"]]

ax.bar(df_students["Student"], df_students["Average"], color=colors)
ax.set_title("Середній бал студентів")
ax.set_xlabel("Студент")
ax.set_ylabel("Середній бал")
ax.axhline(50, color="black", linestyle="--", label="Прохідний бал")

# Додаємо мітки на стовпчики
for i, avg in enumerate(df_students["Average"]):
    ax.text(i, avg + 1, f"{avg:.1f}", ha="center", fontsize=12, color="black")

ax.legend()
plt.show()
