import datetime, time
from dateutil.parser import parse
from maticalgo_data import login
from ohlcv_model import ohlcv
import pandas as pd
import json

ma = login("simha.happy@gmail.com", "491358")
dates = ma.get_dates("banknifty")
for i in dates: 
    latest_date = datetime.datetime.strptime(i, "%Y%m%d").date()    
nse_dates = [datetime.datetime.strptime(i, "%Y%m%d") for i in dates]
print(nse_dates[-1:])
data_obj = ma.get_data("banknifty", latest_date)
df = pd.DataFrame(data_obj)
df_latest = df[-1:]
df_latest["close", "open", "high", "low", "oi", "volume"] = df_latest["close", "open", "high", "low", "oi", "volume"].astype(float)
df_latest["date"]  = pd.to_datetime(df_latest["date"])
df_latest["time"] = df_latest["time"].astype(time)

print(ohlcv.parse_obj(df_latest))

#ohlcv.parse_obj(json_data) 

#collection_of_instances = [ohlcv.parse_obj(item) for item in json_data]
