import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np

ticker_any = input('ticker: ')
ticker_any = ticker_any.upper()
og_link = "https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch"
stock_link = "https://finance.yahoo.com/quote/" + ticker_any + "?p=" + ticker_any + "&.tsrc=fin-srch"
csv_link = "https://query1.finance.yahoo.com/v7/finance/download/" + ticker_any + "?period1=-252374400&period2=1635206400&interval=1d&events=history&includeAdjustedClose=true"

df = pd.read_csv(csv_link)

data = df

bruh = pd.DataFrame(df)


print(bruh.iloc[[-1]])

new_high = input('Latest High: ')
new_low = input('Latest Low: ')

High=pd.DataFrame(data['High'])
Low=pd.DataFrame(data['Low'])
lm = linear_model.LinearRegression()
model = lm.fit(High, Low)
import numpy as np

High_new=np.array([float(new_high)])
Low_new=np.array([float(new_low)])
High_new = High_new.reshape(-1,1)
Low_new = Low_new.reshape(-1,1)
High_predict=model.predict(High_new)
Low_predict=model.predict(Low_new)
print("Predicted High: ")
print(High_predict)
print("Predicted Low: ")
print(Low_predict)
print("Model Score: ")
print(model.score(High, Low)) 

data.plot(kind='scatter', x='High', y='Low')

plt.scatter(High,Low)
plt.plot(High, Low, '.r-')
plt.show()
