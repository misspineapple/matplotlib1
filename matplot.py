import matplotlib.pyplot as plt
years = [2010, 2012, 2014, 2016, 2018, 2020]
population = [10, 12, 15, 18, 20, 22]
plt.plot(years, population, marker='o')
plt.xlabel('Year')
plt.ylabel('Population (in millions)')
plt.title('City Population Over the Years')
plt.show()
