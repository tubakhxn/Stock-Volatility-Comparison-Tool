import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def fetch_data(tickers, start_date, end_date):
    raw_data = yf.download(tickers, start=start_date, end=end_date)
    print("DEBUG: Columns returned:", raw_data.columns)
    # Try to extract 'Adj Close' or fallback to 'Close'
    if isinstance(raw_data.columns, pd.MultiIndex):
        price_level = raw_data.columns.get_level_values(0)
        if 'Adj Close' in price_level:
            data = raw_data['Adj Close']
        elif 'Close' in price_level:
            data = raw_data['Close']
        else:
            raise ValueError("Neither 'Adj Close' nor 'Close' found in downloaded data. Check ticker symbols and date range.")
    else:
        if 'Adj Close' in raw_data.columns:
            data = raw_data[['Adj Close']]
            data.columns = [tickers[0]]
        elif 'Close' in raw_data.columns:
            data = raw_data[['Close']]
            data.columns = [tickers[0]]
        else:
            raise ValueError("Neither 'Adj Close' nor 'Close' found in downloaded data. Check ticker symbols and date range.")
    return data

def calculate_daily_returns(data):
    return data.pct_change().dropna()

def calculate_volatility(daily_returns):
    return daily_returns.std()

def plot_volatility(volatility, chart_type="bar"):
    plt.figure(figsize=(10, 6))
    if chart_type == "bar":
        plt.bar(volatility.index, volatility.values, color="skyblue")
    else:
        plt.plot(volatility.index, volatility.values, marker="o", linestyle="-")
    plt.title("Stock Volatility Comparison")
    plt.xlabel("Stock Ticker")
    plt.ylabel("Volatility (Std Dev of Daily Returns)")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()

def main():
    print("Stock Volatility Comparison Tool")
    tickers = input("Enter stock tickers separated by commas (e.g. AAPL,MSFT,GOOGL): ").upper().replace(" ", "").split(",")
    start_date = input("Enter start date (YYYY-MM-DD): ")
    end_date = input("Enter end date (YYYY-MM-DD): ")
    chart_type = input("Chart type - 'bar' or 'line' [bar]: ").strip().lower() or "bar"

    try:
        data = fetch_data(tickers, start_date, end_date)
    except Exception as e:
        print("Error fetching data:", e)
        return
    daily_returns = calculate_daily_returns(data)
    volatility = calculate_volatility(daily_returns)
    plot_volatility(volatility, chart_type)

if __name__ == "__main__":
    main()
