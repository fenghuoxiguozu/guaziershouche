from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

df=pd.read_csv(r'F:\guaziershouche\cleaned_data.csv')
df=df.round(0)

# def get_brand_num(brand):
#     return np.argwhere(df['car_brand'].unique()==brand)[0][0]
# df['car_brand']=df['car_brand'].map(get_brand_num)
# df=df[['car_brand','buy_year','mile','sale_price','original_price']

x_data=df[['buy_year','mile','original_price']].values.tolist()
x_data=np.array(x_data)
y_data=df['sale_price'].tolist()
sum=len(y_data)
y_data=np.array(y_data)
print(x_data,y_data)

knn=KNeighborsClassifier()
# x_train,x_test,y_train,y_test=train_test_split(x_data,y_data,train_size=0.8)
knn.fit(x_data,y_data)


# brand_input=input("请输入品牌:")
# year_input=input("请输入购买年份:")
# mile_input=input("请输入行驶公里数:")
# price_input=input("请输入购买价格:")

# test_data=[[year_input,mile_input,price_input]]
test_data=[[2015,1,30]]
result=knn.predict(test_data)
print("预测价格为:",result)

