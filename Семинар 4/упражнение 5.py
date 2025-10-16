import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('BTC_data.csv')

df['time'] = pd.to_datetime(df['time'])

df = df.sort_values('time')


plt.figure(figsize=(14, 7))
plt.plot(df['time'], df['close'], linewidth=1)


plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%y'))

# Настройка внешнего вида
plt.xlabel('Дата (DD-MM-YY)')
plt.ylabel('Цена закрытия (USD)')
plt.title('Историческая цена Bitcoin (2018-2023)')
plt.grid(True, alpha=0.3)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()