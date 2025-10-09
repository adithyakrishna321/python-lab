import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
array={'Fruits':['mango', 'orange', 'apple', 'pear', 'banana'], 'Sales':[10, 40, 50, 30, 20]}
fruits=pd.DataFrame(array)
dataset= "fruits_sales.csv"
fruits.to_csv(dataset,index=False)
print(fruits)
plt.figure(figsize=(6,4))
plt.title('Fruits Sales Bar Chart')
plt.xlabel('Fruits')
plt.ylabel('Sales')
plt.bar(fruits['Fruits'], fruits['Sales'])
plt.show()


plt.figure(figsize=(6,4))
plt.scatter(fruits['Sales'], fruits['Fruits'])
plt.show()


age=np.random.choice(range(10,80),size=50)
plt.figure(figsize=(6,4))
plt.hist(age,bins=5)
plt.show()