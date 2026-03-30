import pandas as pd
def load_dataset():
    data={"distance":[2,5,3,6,4,7,8,3,6,2.5,4.5,5.5,7.5],"time":[30,60,40,45,50,35,40,45,50,35,55,50,45],"weight":[60,70,65,75,68,80,85,62,72,64,69,73,82],"height":[1.6,1.7,1.65,1.75,1.68,1.8,1.78,1.62,1.72,1.66,1.69,1.74,1.77],"activity":[1,1,1,2,2,2,2,3,3,3,1,2,3]}
    df=pd.DataFrame(data)
    df["bmi"]=df["weight"]/(df["height"]**2)
    cal=[]
    for i in range(len(df)):
        d=df.loc[i,"distance"]
        w=df.loc[i,"weight"]
        a=df.loc[i,"activity"]
        if a==1:
            c=d*w*0.9
        elif a==2:
            c=d*w*1.6
        else:
            c=d*w*0.8
        cal.append(c)
    df["calories"]=cal
    return df
