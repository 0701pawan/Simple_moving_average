import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators


api_key = 'MQH3XTZ53ASTQ7EA'
### Setting api_key ####

ts = TimeSeries(key=api_key, output_format='pandas') 
##### This helps us to set output format as pandas data frame ####

data_ts, meta_data_ts = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')
 #### This will take set interval at what time we need take closing stock price###

period = 60 
#Setting period

ti = TechIndicators(key=api_key, output_format='pandas')
##### This helps us to set output format as pandas data frame ####

data_ti, meta_data_ti = ti.get_sma(symbol='MSFT', interval='1min', time_period=period, series_type='close')
##### This will take set interval and period at what which we want to calculate the SMA ####



df1 = data_ti
df2 = data_ts['4. close'].iloc[period-1::] ###### This helps in showing only the last closing price at which period ends ####

### This helps in setting the output format ####
df2.index = df1.index

total_df = pd.concat([df1, df2], axis=1)
print(total_df)


