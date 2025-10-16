import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

d = pd.read_csv("BTC_data.csv")
d["time"] = pd.to_datetime(d["time"])

x = np.arange(len(d))
y = d["close"].values

deg = 30
coefficients = np.polyfit(x, y, deg)
polynomial = np.poly1d(coefficients)

plt.figure(figsize=(12, 6))
plt.plot(d["time"], y, label="Реальная цена", linewidth=1, alpha=0.7)
plt.plot(d["time"], polynomial(x), color="red", linewidth=2, label=f"Полином {deg}-й степени")

plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%d-%m-%y'))

plt.xlabel("Дата")
plt.ylabel("Цена закрытия (USD)")
plt.title("Bitcoin: реальная цена и полиномиальная аппроксимация")
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print(f"Полином {deg}-й степени:")
print(polynomial)