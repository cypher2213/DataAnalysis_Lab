import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('comptagevelo2017.csv')

print(df.columns)

# Конвертуємо дату
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df['Month'] = df['Date'].dt.month


count_cols = df.select_dtypes(include='number').columns # Беремо всі станції

print(df.head())
print(df.info())
print(df.describe())

total_year_all = df[count_cols].sum().sum() # Загальна кількість велосипедистів
print("Загальна кількість велосипедистів за рік (усі доріжки):", total_year_all)

# По кожній доріжці
total_year_per_lane = df[count_cols].sum()
print("Загальна кількість велосипедистів за рік по кожній доріжці:")
print(total_year_per_lane)

lanes = ['Eco-Totem - Métro Laurier', 'Parc', 'Notre-Dame']

for lane in lanes:
    if lane in df.columns:
        popular_month = df.groupby('Month')[lane].sum().idxmax()
        print(f"Найпопулярніший місяць для {lane}: {popular_month}")
    else:
        print(f"Колонки {lane} немає у файлі!")

# Графік Eco-Totem - Métro Laurier
monthly = df.groupby('Month')['Eco-Totem - Métro Laurier'].sum()

plt.plot(monthly)
plt.title("Завантаженість велодоріжки Eco-Totem - Métro Laurier по місяцях")
plt.xlabel("Місяць")
plt.ylabel("Кількість велосипедистів")
plt.grid(True)
plt.show()
