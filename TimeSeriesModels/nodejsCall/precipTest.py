##### Prophet section (start) ##########################################################################
### module imports (start) ##########################################################
import os
import sys
import time
import random
import string

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb 
from pylab import rcParams
import scipy
from scipy.stats import pearsonr

from prophet import Prophet
import json
from prophet.plot import plot_plotly, plot_components_plotly

from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.stattools import adfuller
#                                       \/
#                   The Augmented Dickey-Fuller test can be used to test 
#                   whether a given time series is stationary or not
from sklearn.metrics import mean_squared_error
from tqdm import tqdm_notebook
#                    \/
#       responsible for displaying the progress bar
from itertools import product

import warnings
warnings.filterwarnings('ignore')
plt.rcParams['figure.figsize'] = [10,10]

### module imports (end) ############################################################
                                                   
### calling the csv data (start) ####################################################
# precip1 = pd.read_csv('/Users/stephenshaeffer/Desktop/TXT-CSV/precipitation_station1.txt')
# Load JSON data
with open('/Users/stephenshaeffer/Desktop/TXT-CSV/precipitation_station1.json', 'r') as file:
    json_data = json.load(file)

# Convert JSON data to DataFrame
precip1 = pd.DataFrame(json_data)

### defining the "m" method ###

m = Prophet()
m.fit(precip1)

### defining prediction data frames ###

precipDayfuture = m.make_future_dataframe(periods=1)

precipWeekfuture = m.make_future_dataframe(periods=7)

precip2Weekfuture = m.make_future_dataframe(periods=14)

### utilizing prediction data frames ###

precipDayforecast = m.predict(precipDayfuture)
precipDayforecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

# after generating the forecast data, convert it to JSON
forecast_data_precipDay = {
    'ds': precipDayforecast['ds'].dt.strftime('%Y-%m-%d').tolist(),
    'yhat': precipDayforecast['yhat'].tolist(),
    'yhat_lower': precipDayforecast['yhat_lower'].tolist(),
    'yhat_upper': precipDayforecast['yhat_upper'].tolist()
}

# Write forecast data to JSON files for each timeframe
precipWeekforecast = m.predict(precipWeekfuture)
precipWeekforecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

forecast_data_precipWeek = {
    'ds': precipWeekforecast['ds'].dt.strftime('%Y-%m-%d').tolist(),
    'yhat': precipWeekforecast['yhat'].tolist(),
    'yhat_lower': precipWeekforecast['yhat_lower'].tolist(),
    'yhat_upper': precipWeekforecast['yhat_upper'].tolist()
}

precip2Weekforecast = m.predict(precip2Weekfuture)
precip2Weekforecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

forecast_data_precip2Week = {
    'ds': precip2Weekforecast['ds'].dt.strftime('%Y-%m-%d').tolist(),
    'yhat': precip2Weekforecast['yhat'].tolist(),
    'yhat_lower': precip2Weekforecast['yhat_lower'].tolist(),
    'yhat_upper': precip2Weekforecast['yhat_upper'].tolist()
}

with open('forecast_data_day.json', 'w') as file:
    json.dump(forecast_data_precipDay, file)

with open('forecast_data_week.json', 'w') as file:
    json.dump(forecast_data_precipWeek, file)

with open('forecast_data_2week.json', 'w') as file:
    json.dump(forecast_data_precip2Week, file)

### plotting the 24 hour forcasting (start) ##########################################################
def day_graph_1(m, precipDayforecast):
    return m.plot(precipDayforecast)

def day_graph_2(m, precipDayforecast):
    return m.plot_components(precipDayforecast)

def day_graph_3(m, precipDayforecast):
    return plot_plotly(m, precipDayforecast)

def day_graph_4(m, precipDayforecast):
    return plot_components_plotly(m, precipDayforecast)
### plotting the 24 hour forcasting (end) ##########################################################
### plotting the weekly forcasting (start) ##########################################################
def week_graph_1(m, precipWeekforecast):
    return m.plot(precipWeekforecast)

def week_graph_2(m, precipWeekforecast):
    return m.plot_components(precipWeekforecast)

def week_graph_3(m, precipWeekforecast):
    return plot_plotly(m, precipWeekforecast)

def week_graph_4(m, precipWeekforecast):
    return plot_components_plotly(m, precipWeekforecast)
### plotting the weekly forcasting (end) ##########################################################
### plotting the 2 week forcasting (start) ##########################################################
def two_week_graph_1(m, precip2Weekforecast):
    return m.plot(precip2Weekforecast)

def two_week_graph_2(m, precip2Weekforecast):
    return m.plot_components(precip2Weekforecast)

def two_week_graph_3(m, precip2Weekforecast):
    return plot_plotly(m, precip2Weekforecast)

def two_week_graph_4(m, precip2Weekforecast):
    return plot_components_plotly(m, precip2Weekforecast)
### plotting the 2 week forcasting (end) ##########################################################

##### ARIMA section (start) ##########################################################################
### plotting the data (start) ##########################################################
def ARIMA_plot():
    plt.plot(precip1['ds'], precip1['y'])
    plt.ylabel('Precipitation')
    plt.xlabel('Date')
    plt.xticks(rotation=30)
    plt.rcParams['figure.figsize'] = [10, 10]

    # Save the plot as an image
    image_path = '/Users/stephenshaeffer/Desktop/test123321'
    plt.savefig(image_path)

    return image_path

def ARIMA_plot():
    plt.plot(precip1['ds'], precip1['y'])
    plt.ylabel('Precipitation')
    plt.xlabel('Date')
    plt.xticks(rotation=30)
    plt.rcParams['figure.figsize'] = [10, 10]

    # Save the plot as an image
    plt.savefig('plot.png')

if __name__ == "__main__":
    # Call the appropriate function based on the command
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == 'ARIMA_plot':
            ARIMA_plot()
    else:
        print("No command provided.")
### plotting the data (end) ##########################################################
### testing for stationary (start) ##########################################################
"""
testing for unit root with ACF

"""
def stationarity_test1():
# a1 and c1 are for the ranges of p that should be acceptable
    a1 = 0.001
    a2 = 0.01
    b1 = 0.05
    b2 = 0.001
    c1 = 0.10

    ad_fuller_result = adfuller(precip1['y'])

    p = (ad_fuller_result[1])
    
    ADF1 = (ad_fuller_result[0])
    p1 = (ad_fuller_result[1])

    precip1['log_diff'] = np.log(precip1['y']) # taking that log of the data 
    precip1['log_diff'] = precip1['log_diff'].diff() # taking the difference of the log data
    ad_fuller_result2 = adfuller(precip1['log_diff'][1:])

    ADF2 = (ad_fuller_result2[0])
    p2 = (ad_fuller_result2[1])

    if ((ADF2 and p2) < (ADF1 and p1)) and ((p2 < a1) or (a1 < p2 < a2) or (b1 < p2 < b2)):
        print('this is stationary\n ADF                p-value')
        return ADF2, p2
    elif (ADF2 and p2) > (ADF1 and p1) and ((p1 < a1) or (a1 < p1 < a2) or (b1 < p1 < b2)):
        print('this is stationary\n ADF                p-value')
        return ADF2, p2

stationarity_test1()
### testing for stationary (end) ##########################################################
### determining best parameters with AIC and the fitting then best model (start) ##########################################################
"""
AR: order of 0-10
I: equals 1 (since we only difference once)
MA: order of 0-10
"""
def optimize_ARIMA(endog, order_list):
    """
        Return dataframe with parameters and corresponding AIC (Akaike Information Criterion)
                                                            ^
                                            This is an estimator of prediction error
        order_list - list with (p, d, q) tuples
        endog - the observed variable
    """
    
    results = []
    
    for order in tqdm_notebook(order_list):
        try: 
            model = SARIMAX(endog, order=order, simple_differencing=False).fit(disp=False)
        except:
            continue
            
        aic = model.aic
        results.append([order, model.aic])
        
    result_df = pd.DataFrame(results)
    result_df.columns = ['(p, d, q)', 'AIC']
    #Sort in ascending order, lower AIC is better
    result_df = result_df.sort_values(by='AIC', ascending=True).reset_index(drop=True)
    
    return result_df
### determining best parameters with AIC and the fitting then best model (end) ##########################################################
### evaluating forecasting results of the model (start) ##########################################################
"""
forecasting a predicted mean value
"""
n_forecast = 1000
predict = res.get_prediction(end=best_model1.nobs + n_forecast)
#                                            /\
#                           this means number of observations 
idx1 = np.arange(len(predict.predicted_mean))

fig, ax = plt.subplots()
ax.plot(precip1['y'], 'blue')
ax.plot(idx1[-n_forecast:], predict.predicted_mean[-n_forecast:], 'y--')

ax.set(title = 'Precipitation Forecast 1')
plt.show()

precip1['model'] = predict.predicted_mean
precip1
### evaluating forecasting results of the model (end) ##########################################################
### taking into account mean squared error value for the model (start) ##########################################################
mse = mean_squared_error(precip1['y'], precip1['model'])
print(f'MSE: {mse}')
### taking into account mean squared error value for the model (end) ##########################################################
##### ARIMA section (end) ##########################################################################
##### ARIMA section (end) ##########################################################################