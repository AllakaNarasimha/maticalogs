##Creating an Account using the above url (Create an account)

from maticalgos.historical import historical
import datetime
import pandas as pd
import csv

ma = historical('simha.happy@gmail.com')
#ma.reset_password() 
## New Password will be sent to your registered email ID
ma.login("491358") ##Password as sent on email 

startDate = datetime.date(2018,1,15)
data = ma.get_dates("banknifty") 
print (data)

df = pd.DataFrame(data)
csv_file_path = "banknifty_"+ startDate.strftime('%d%m%Y')+".csv"

# Writing DataFrame to CSV file
df.to_csv(csv_file_path, index=False)
    
#Data available only for nifty options from 2019 and banknifty options from 2018
#Date should be in datetime.date format
#Data would be in pandas DataFrame format