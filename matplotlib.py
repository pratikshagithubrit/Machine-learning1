import pandas as pd
import matplotlib.pyplot as plt
excel_file='marvellous.xlsx'
data=pd.read_excel(excel_file)

print("all data from excel file")
print(data)

print("first 5 rows from file")
print(data.head())

print("first 4 rows from file")
print(data.head(4))

print("last 5 rows from file")
print(data.tail(3))

print("last 4 rows from file")
print(data.tail(4))

print(data.shape)

Sorted_data=data.sort_Values(['Name'],ascending=False)
print("sorted data")
print(sorted_data)

data['Age'].plot(kind="hist")
plt.show()

data['Age'].plot(kind="barh")
plt.show()


