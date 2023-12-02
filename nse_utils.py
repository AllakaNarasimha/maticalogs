# nse_utils.py
from nsepy import get_history
from datetime import datetime

def is_nse_holiday(date_to_check):
    try:
        data = get_history(symbol="RELIANCE", start=date_to_check, end=date_to_check)
        return data.empty
    except Exception:
        return False
def get_nse_history(symbol, start_date, end_date):
    #vix = get_history(symbol="INDIAVIX",
    #        start=date(2015,1,1),
    #        end=date(2015,1,10),
    #        index=True)
    vix = get_history(symbol=symbol,
            start_date,
            end_date,
            index=True) 
    return vix   