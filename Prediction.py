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
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
from sklearn import linear_model



def Predict():
	mse=[]
	mae=[]
	rsq=[]
	rmse=[]
	acy=[]

	df=pd.read_csv("bitcoin.csv")
	print(df)

	train = df[:1800][[ 'Open', 'High', 'Low','Close','Volume (BTC)','Volume (Currency)','Weighted Price']]
	test = df[1801:][[ 'Open', 'High', 'Low','Close','Volume (BTC)','Volume (Currency)','Weighted Price']]

	X_train =train[[ 'Open', 'High', 'Low','Volume (BTC)','Volume (Currency)','Weighted Price']]
	y_train =train[['Close']]




	X_test =test[[ 'Open', 'High', 'Low','Volume (BTC)','Volume (Currency)','Weighted Price']]
	y_test =test[['Close']]


	clf = linear_model.Lasso(alpha = 0.1)
	clf.fit(X_train, y_train)
	y = clf.predict(X_test)

	print("MSE VALUE FOR Lasso IS %f "  % mean_squared_error(y_test,y))
	print("MAE VALUE FOR Lasso IS %f "  % mean_absolute_error(y_test,y))
	print("R-SQUARED VALUE FOR Lasso IS %f "  % r2_score(y_test,y))
	rms = np.sqrt(mean_squared_error(y_test,y))
	print("RMSE VALUE FOR Lasso IS %f "  % rms)
	ac = clf.score(X_test, y_test) * 100
	print ("ACCURACY VALUE Lasso IS %f" % ac)

	mse.append(mean_squared_error(y_test,y))
	mae.append(mean_absolute_error(y_test,y))
	rsq.append(r2_score(y_test,y))
	rmse.append(rms)
	acy.append(ac)



	x = np.arange(len(X_test))
	plt.plot(x, y_test,label='Original Vale')
	plt.plot(x, y,label='Predicted Value')
	plt.legend()
	plt.title('Original Value vs Predicted Value In Lasso ')
	plt.xlabel("Day (s)")
	plt.ylabel("Predicted Value")
	
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	clf = linear_model.LinearRegression()
	clf.fit(X_train, y_train)
	y = clf.predict(X_test)
	
	print("MSE VALUE FOR Regression IS %f "  % mean_squared_error(y_test,y))
	print("MAE VALUE FOR Regression IS %f "  % mean_absolute_error(y_test,y))
	print("R-SQUARED VALUE FOR Regression IS %f "  % r2_score(y_test,y))
	rms = np.sqrt(mean_squared_error(y_test,y))
	print("RMSE VALUE FOR Regression IS %f "  % rms)
	ac = clf.score(X_test, y_test) * 100
	print ("ACCURACY VALUE Regression IS %f" % ac)

	mse.append(mean_squared_error(y_test,y))
	mae.append(mean_absolute_error(y_test,y))
	rsq.append(r2_score(y_test,y))
	rmse.append(rms)
	acy.append(ac)



	x = np.arange(len(X_test))
	plt.plot(x, y_test,label='Original Vale')
	plt.plot(x, y,label='Predicted Value')
	plt.legend()
	plt.title('Original Value vs Predicted Value In Regression ')
	plt.xlabel("Day (s)")
	plt.ylabel("Predicted Value")
	plt.pause(5)
	plt.show(block=False)
	plt.close()


	al = ['Lasso','Regression']
    
    
	result2=open('MSE.csv', 'w')
	result2.write("Algorithm,MSE" + "\n")
	for i in range(0,len(mse)):
	    result2.write(al[i] + "," +str(mse[i]) + "\n")
	result2.close()
    
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
       
    
	#Barplot for the dependent variable
	fig = plt.figure(0)
	df =  pd.read_csv('MSE.csv')
	acc = df["MSE"]
	alc = df["Algorithm"]
	plt.bar(alc,acc,align='center', alpha=0.5,color=colors)
	plt.xlabel('Algorithm')
	plt.ylabel('MSE')
	plt.title("MSE Value");
	fig.savefig('MSE.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()

    
    
    
	result2=open('MAE.csv', 'w')
	result2.write("Algorithm,MAE" + "\n")
	for i in range(0,len(mae)):
	    result2.write(al[i] + "," +str(mae[i]) + "\n")
	result2.close()
                
	fig = plt.figure(0)            
	df =  pd.read_csv('MAE.csv')
	acc = df["MAE"]
	alc = df["Algorithm"]
	plt.bar(alc,acc,align='center', alpha=0.5,color=colors)
	plt.xlabel('Algorithm')
	plt.ylabel('MAE')
	plt.title('MAE Value')
	fig.savefig('MAE.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()

    
	result2=open('R-SQUARED.csv', 'w')
	result2.write("Algorithm,R-SQUARED" + "\n")
	for i in range(0,len(rsq)):
	    result2.write(al[i] + "," +str(rsq[i]) + "\n")
	result2.close()
            
	fig = plt.figure(0)        
	df =  pd.read_csv('R-SQUARED.csv')
	acc = df["R-SQUARED"]
	alc = df["Algorithm"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	plt.bar(alc,acc,align='center', alpha=0.5,color=colors)
	plt.xlabel('Algorithm')
	plt.ylabel('R-SQUARED')
	plt.title('R-SQUARED Value')
	fig.savefig('R-SQUARED.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()

    
	result2=open('RMSE.csv', 'w')
	result2.write("Algorithm,RMSE" + "\n")
	for i in range(0,len(rmse)):
	    result2.write(al[i] + "," +str(rmse[i]) + "\n")
	result2.close()
      
	fig = plt.figure(0)    
	df =  pd.read_csv('RMSE.csv')
	acc = df["RMSE"]
	alc = df["Algorithm"]
	plt.bar(alc, acc, align='center', alpha=0.5,color=colors)
	plt.xlabel('Algorithm')
	plt.ylabel('RMSE')
	plt.title('RMSE Value')
	fig.savefig('RMSE.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()

    
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

    






    



