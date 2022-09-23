import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("data2.csv").to_numpy() 

x = data[:, 0]
y = data[:, 1]

app = plt.plot(x, y)

