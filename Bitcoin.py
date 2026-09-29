import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing,svm
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import time


def getPrice(sym):
	forecastAccu = []
	shareList1 = []
	shareList2 = []
	finalForecastPrice = []
	count = 0
	#BITSTAMPUSD
	symbol="BCHARTS/"+sym
	print(symbol)
	df = quandl.get(symbol, authtoken="TyoiVKMxwYyUoh-ic92A")
	df.dropna(inplace = True)
	print(df)
	df.to_csv("bitcoin.csv")
	print(df.index)
	date_list = np.array(df.index.to_pydatetime())
	print(date_list)
	plot_array = np.zeros([len(df), 5])
	plot_array[:, 0] = np.arange(plot_array.shape[0])
	print(df.iloc[:, 1:5])
	plot_array[:, 1:] = df.iloc[:, 1:5]
	# plotting candlestick chart
	fig, ax = plt.subplots(figsize=(18, 18))
	num_of_bars = 1000  # the number of candlesticks to be plotted
	candlestick_ohlc(ax, plot_array[-num_of_bars:], colorup='g', colordown='r')
	ax.margins(x=0.0, y=0.1)
	ax.yaxis.tick_right()
	x_tick_labels = []
	ax.set_xlim(right=plot_array[-1, 0]+10)
	ax.grid(True, color='k', ls='--', alpha=0.2)
	# setting xticklabels actual dates instead of numbers
	indices = np.linspace(plot_array[-num_of_bars, 0], plot_array[-1, 0], 8, dtype=int)
	for i in indices:
		date_dt = df.index[i]
		date_str = date_dt.strftime('%b-%d')
		x_tick_labels.append(date_str)

	ax.set(xticks=indices, xticklabels=x_tick_labels)
	plt.title("BitCoin Price")
	ax.set_xlabel('Date')
	ax.set_ylabel('price')
	plt.savefig("BitCoin Price.png")
	plt.pause(5)
	plt.show(block=False)
	plt.close()
      
getPrice("BITSTAMPUSD")