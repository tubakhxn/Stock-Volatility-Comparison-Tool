
# Stock Volatility Comparison Tool
Developer & Creator: tubakhxn

## About This Project
This tool lets you compare the volatility of multiple stocks using historical price data. It fetches data from Yahoo Finance, calculates daily returns, computes volatility, and visualizes the results in a clear chart. Great for anyone wanting to see which stocks are more stable or risky over time.

## What is Volatility?
Volatility is a statistical measure of the dispersion of returns for a given stock. In simple terms, it tells you how much the price of a stock moves up or down over a period of time. Higher volatility means the stock price changes a lot, while lower volatility means it stays more stable.

## How is Volatility Calculated?
Volatility is commonly calculated as the standard deviation of daily returns. Daily returns are the percentage change in price from one day to the next. The standard deviation measures how much these returns deviate from their average value.

**Formula:**

- Daily Return = (Today's Close - Yesterday's Close) / Yesterday's Close
- Volatility = Standard Deviation of Daily Returns

## How to Interpret the Volatility Graph
- Each bar or line on the graph represents the volatility of a stock over the selected period.
- Higher bars/lines indicate more volatile stocks (greater price swings).
- Lower bars/lines indicate more stable stocks (smaller price swings).

## Setup and Execution Steps

1. **Clone or download this repository.**
2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```
3. **Run the tool:**
   ```
   python volatility.py
   ```
4. **Follow the prompts to enter stock tickers and date range.**

The tool will fetch historical data, calculate volatility, and display a comparison chart.

## How to Fork This Project
1. Click the "Fork" button at the top right of the GitHub page.
2. Clone your forked repository:
   ```
   git clone https://github.com/yourusername/Stock-Volatility-Comparison-Tool.git
   ```
3. Make your changes and push to your fork.
