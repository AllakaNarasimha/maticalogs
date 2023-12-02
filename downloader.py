import os
import datetime
from dateutil.parser import parse
import pandas as pd
from maticalgo_data import login
from nse_utils import is_nse_holiday

def get_week_number(date):
    return date.strftime('%U')

def get_week_folder(base_path, year, date):
    week_number = get_week_number(date)
    week_folder = os.path.join(base_path, f"Week_{year}_{week_number}")

    if os.path.exists(week_folder):
        return week_folder
    else:
        print(f"Week folder {week_folder} does not exist.")
        return None
    
def create_year_week_folder(base_path, year, week_number):
    week_folder = os.path.join(base_path, f"Week_{year}_{week_number}")

    if not os.path.exists(week_folder):
        os.makedirs(week_folder)
    return week_folder
    
def create_week_folder(base_path, week_number):
    week_folder = os.path.join(base_path, f"Week_{week_number}")

    if not os.path.exists(week_folder):
        os.makedirs(week_folder)

    return week_folder

def process_date_range(start_date, end_date):
    current_date = start_date    
    while current_date <= end_date:
        isholiday = is_nse_holiday(current_date)
        if isholiday:
            current_date += datetime.timedelta(days=1)
            continue
        download(current_date)
        # Increment the current date by one day
        current_date += datetime.timedelta(days=1)
        
def download(current_date):
    # Call your processing logic or method here
    try:
        data = ma.get_data("banknifty", current_date) 
    except Exception as e:
        current_date += datetime.timedelta(days=1)
        return
        
    print(current_date.strftime('%Y-%m-%d_%A'))        
    df = pd.DataFrame(data)
    week_number = get_week_number(current_date)
    year = current_date.year
    week_folder = create_year_week_folder("", year, week_number)        
    file_name = "banknifty_"+ current_date.strftime('%d%m%Y_%A')+".csv"
    csv_file_path = os.path.join(week_folder, file_name)
    # Writing DataFrame to CSV file
    df.to_csv(csv_file_path, index=False)
    
# Specify the start and end dates
start_date = datetime.date(2018, 1, 1)
end_date = datetime.date(2018, 1, 10)

ma = login("simha.happy@gmail.com", "491358")
dates = ma.get_dates("banknifty")
cutoff_date = datetime.date(2022, 2, 3)
# Filter date strings before the cutoff date
filtered_dates = [i for i in dates if datetime.datetime.strptime(i, "%Y%m%d").date() < cutoff_date]
reverse_dates = filtered_dates.copy()
reverse_dates.reverse()
for i in reverse_dates: 
    latest_date = datetime.datetime.strptime(i, "%Y%m%d").date()    
    # Call the method to process the date range
    download(latest_date)
#process_date_range(start_date, end_date)