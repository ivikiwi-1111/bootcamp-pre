import pandas as pd 
import matplotlib.pyplot as plt 

data = pd.read_csv("data1.txt").to_numpy() 

app = plt.plot(data)
