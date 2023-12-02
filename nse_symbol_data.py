import yfinance as yf

def get_indiavix_data():
    indiavix_ticker = "^INDIAVIX"

    # Download historical data for India VIX
    indiavix_data = yf.download(indiavix_ticker, start="2023-01-01", end="2023-01-31")

    return indiavix_data

# Get India VIX data
indiavix_data = get_indiavix_data()

# Print the India VIX data
print("India VIX Data:")
print(indiavix_data)
