from sklearn.linear_model import LinearRegression
def train_model(df):
    x=df[["distance","time","weight","bmi","activity"]]
    y=df["calories"]
    m=LinearRegression()
    m.fit(x,y)
    return m,x,y
