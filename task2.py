# Задача 2. Имеются данные о площади и стоимости 15 домов.
# Риелтору требуется узнать в каких домах стоимость квадратного метра меньше 50000 рублей.
# Предоставьте ему графические данные о стоимости квадратного метра каждого дома и список подходящих ему домов, 
# отсортированных по площади.
# Данные о домах сформируйте случайным образом. Площади от 100 до 300 кв. метров, цены от 3 до 20 млн.

from matplotlib import pyplot as plt  
import random
from matplotlib.pyplot import MultipleLocator


housesArea = [random.randint(100, 300) for i in range(0,15)]
housesPrice = [random.randint(3000000, 20000000) for i in range(0,15)]
x = []
costPerMeter = []
lowPrice = []
sortedHouses = []

for i in range(0,15):
    x.append(i+1)

for i in range(len(housesArea)):
    costPerMeter.append(round(housesPrice[i]/housesArea[i]))


print(housesArea)
print(costPerMeter)


for i in range(len(costPerMeter)):
    if costPerMeter[i] < 50000:
        lowPrice.append(costPerMeter[i])
        sortedHouses.append(housesArea[i])

for i in range(len(sortedHouses)-1):
    for j in range(len(sortedHouses)-i-1):
        if sortedHouses[j] > sortedHouses[j+1]:
            lowPrice[j], lowPrice[j+1] = lowPrice[j+1], lowPrice[j]
            sortedHouses[j], sortedHouses[j+1] = sortedHouses[j+1], sortedHouses[j]


print('\nДома, стоимость квадратного метра которых меньше 50000 рублей:')
for i in range(len(lowPrice)):
    print(f'Площадь дома: {sortedHouses[i]}, стоимость квадратного метра: {lowPrice[i]}')


plt.title('Стоимость квадратного метра каждого дома')
plt.xlabel('Номер дома')    
plt.ylabel('Стоимость квадратного метра')  
plt.grid(which='major')
x_major_locator=MultipleLocator(1)
ax=plt.gca()
ax.xaxis.set_major_locator(x_major_locator)


plot2 = list(50000 for a in range(1, 16))
plt.plot(x, plot2)
plt.plot(x, costPerMeter, 'go')
plt.show()