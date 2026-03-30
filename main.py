from dataset import load_dataset
from model import train_model
from sklearn.metrics import r2_score
import pandas as pd
import matplotlib.pyplot as plt

df=load_dataset()
m,x,y=train_model(df)
print("Fitness Calorie Predictor")
print("1 Walking 2 Running 3 Cycling")

d=float(input("Distance(km): "))
t=float(input("Time(min): "))
w=float(input("Weight(kg): "))
h=float(input("Height(m): "))
a=int(input("Activity(1/2/3): "))
b=w/(h**2)
print("BMI:",round(b,2))
inp=pd.DataFrame([[d,t,w,b,a]],columns=['distance','time','weight','bmi','activity'])
p=m.predict(inp)
print("Calories:",round(p[0],2))
acc=r2_score(y,m.predict(x))
print("Accuracy:",round(acc,2))
plt.scatter(df['distance'],df['calories'])
plt.xlabel("Distance")
plt.ylabel("Calories")
plt.title("Distance vs Calories")
plt.show()
