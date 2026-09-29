import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing,svm
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
from sklearn import tree
from sklearn.linear_model import LinearRegression


def Forcast():
	acy=[]
	df=pd.read_csv("bitcoin.csv")
	print(df)
	df = df[['Open','High','Low','Close']]
	df['HL_PCT'] =(df['High'] - df['Close'])/df['Close'] * 100.0
	df['PCT_Change'] =(df['Close'] - df['Open'])/df['Open'] * 100.0
	df = df[['Close','HL_PCT','PCT_Change']]
	forecast_col = 'Close'
	df.fillna(-9999999, inplace = True)
	forecast_out = int(5)
	print(forecast_out)
	
	df['label'] = df[forecast_col].shift(-forecast_out)
	X = np.array(df.drop(['label'],axis=1))
	X = preprocessing.scale(X)
	X_lately = X[-forecast_out:]
	X = X[:-forecast_out]

	df.dropna(inplace = True)
	y = np.array(df['label'])
	

	print(X)
	print(y)


	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)




	clf = tree.DecisionTreeRegressor()
	clf.fit(X_train, y_train)
	y = clf.predict(X_lately)
	print("Decision Tree Forcast")
	print(y)
	ac = clf.score(X_test, y_test) * 100
	print ("ACCURACY VALUE Decision Tree IS %f" % ac)
	acy.append(ac)
	print("------------------------------------------------------------------")


	x = np.arange(forecast_out)
	plt.plot(x, y,label='Decission Tree')
	plt.legend()
	plt.title('Decission Tree')
	plt.xlabel("Day (s)")
	plt.ylabel("Predicted Value")
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	clf = LinearRegression(n_jobs = -1)
	clf.fit(X_train, y_train)
	y1 = clf.predict(X_lately)
	print("Regression Tree Forcast")
	print(y1)
	ac = clf.score(X_test, y_test) * 100
	print ("ACCURACY VALUE Regression IS %f" % ac)
	acy.append(ac)
	print("------------------------------------------------------------------")


	x = np.arange(forecast_out)
	plt.plot(x, y1,label='Regression')
	plt.legend()
	plt.title('Regression')
	plt.xlabel("Day (s)")
	plt.ylabel("Predicted Value")
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	
	al = ['DecisionTree','Regression']

	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  


	result2=open('Accuracy.csv', 'w')
	result2.write("Algorithm,Accuracy" + "\n")
	for i in range(0,len(acy)):
	    result2.write(al[i] + "," +str(acy[i]) + "\n")
	result2.close()
    
	fig = plt.figure(0)
	df =  pd.read_csv('Accuracy.csv')
	acc = df["Accuracy"]
	alc = df["Algorithm"]
	plt.bar(alc, acc, align='center', alpha=0.5,color=colors)
	plt.xlabel('Algorithm')
	plt.ylabel('Accuracy')
	plt.title('Accuracy Value')
	fig.savefig('Accuracy.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	x = np.arange(forecast_out)
	plt.plot(x, y,label='Decission Tree')
	plt.plot(x, y1,label='Regression')
	plt.legend()
	plt.title('Decission Tree vs Regression')
	plt.xlabel("Day (s)")
	plt.ylabel("Predicted Value")
	plt.pause(5)
	plt.show(block=False)
	plt.close()