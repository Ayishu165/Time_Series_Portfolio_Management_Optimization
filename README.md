#Time Series Portfolio Management and Optimization 📈

This project demonstrates a comprehensive workflow for financial time series analysis, including data preprocessing, exploratory data analysis (EDA), and time series forecasting. The goal is to build a foundation for an investment strategy by predicting stock market trends and optimizing a multi-asset portfolio.

Project Structure
.
├── data
│   ├── processed/
│   └── raw/
├── notebooks/
│   ├── 01_data_preprocessing_and_eda.ipynb
│   └── 02_time_series_models.ipynb
├── outputs/
│   ├── plots/
│   └── results/
└── README.md

2. Clone the repository:

git clone [repository-url]
cd Time_Series_Portfolio_Management_Optimization

3. Task 1: Preprocess and Explore the Data 📊
The first notebook, 01_data_preprocessing_and_eda.ipynb, is dedicated to data acquisition, cleaning, and an initial exploratory analysis.

Subtask 1.1: Extract Historical Financial Data
Objective: Use the yfinance library to download historical adjusted closing prices for selected assets (TSLA, BND, SPY).

Output: Raw data for each ticker is saved as a CSV file in the data/raw directory.

Subtask 1.2: Data Cleaning and Understanding
Objective: Load the raw data, merge it into a single DataFrame, handle missing values, and save a clean version for subsequent tasks.

Methodology:

Load the raw CSV files.

Extract the Close price column (which represents the adjusted close price).

Handle any missing data by using forward-fill (ffill) and backward-fill (bfill) methods.

Output: The cleaned and merged data is saved as all_assets_processed.csv in the data/processed directory.

Subtask 1.3: Conduct Exploratory Data Analysis (EDA)
Objective: Visualize and analyze the processed data to understand its key characteristics.

Analysis:

Plot the time series of adjusted closing prices for all assets.

Calculate and visualize daily percentage changes (returns).

Analyze volatility using rolling mean and standard deviation plots.

Output: Plots are saved as PNG files in the outputs/plots directory.

Subtask 1.4 & 1.5: Seasonality, Trends, and Risk Metrics
Objective: Formally test for data stationarity and calculate key risk metrics.

Analysis:

Use the Augmented Dickey-Fuller (ADF) test to check if the price series are stationary.

Calculate metrics like overall price change, daily return volatility, and Value at Risk (VaR).

Compute the Sharpe Ratio to assess risk-adjusted returns.

Task 2: Develop Time Series Forecasting Models 🔮
The second notebook, 02_time_series_models.ipynb, focuses on implementing and comparing two popular time series forecasting models.

Subtask 2.1: Implement and Compare Models
Objective: Train at least two different forecasting models on the TSLA stock price data.

Models:

ARIMA (AutoRegressive Integrated Moving Average): A classical statistical model. The auto_arima function is used to automatically find the optimal parameters.

LSTM (Long Short-Term Memory): A type of recurrent neural network particularly effective for sequence data like time series.

Output: The trained LSTM model is saved to outputs/results/lstm_model.keras.

Subtask 2.2: Forecast Future Stock Prices and Compare Predictions
Objective: Use the trained models to forecast stock prices for the test period and evaluate their performance.

Methodology:

Generate predictions for the test set using both the ARIMA and LSTM models.

Evaluate the models using key metrics such as Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Percentage Error (MAPE).

Output: A plot comparing the actual prices with the forecasts from both models is saved, along with the performance metrics in a CSV file.

Task 2: Develop Time Series Forecasting Models 🔮
This task focuses on building predictive models for the TSLA stock price. The 02_time_series_models.ipynb notebook implements and compares two distinct models.

Models Implemented:

ARIMA (AutoRegressive Integrated Moving Average): A classical statistical model optimized using auto_arima to find the best parameters.

LSTM (Long Short-Term Memory): A deep learning model built using tensorflow to capture complex, non-linear patterns in the data.

Process: The TSLA data is split chronologically into training and testing sets. Both models are trained, and their performance is evaluated using metrics like MAE, RMSE, and MAPE on the test set.

Task 3: Forecast Future Market Trends 📈
The 03_forecast_analysis.ipynb notebook uses the best-performing model from Task 2 to generate a forward-looking forecast.

Process:

The trained model (e.g., the LSTM model saved in Task 2) is loaded.

A forecast for the next 6 months of TSLA stock prices is generated.

The forecast is visualized and saved to outputs/results/tsla_future_forecast.csv.

Task 4: Optimize Portfolio Based on Forecast 💼
This task applies Modern Portfolio Theory (MPT) to create an optimal portfolio using a combination of historical data and the TSLA forecast. This is documented in 04_portfolio_optimization.ipynb.

Process:

The annualized expected return for TSLA is overridden with the value derived from the 6-month forecast.

Expected returns and the covariance matrix for all assets (TSLA, BND, SPY) are calculated.

The Efficient Frontier is plotted, and the optimal portfolios (e.g., Maximum Sharpe Ratio and Minimum Volatility) are identified.

The weights of the recommended optimal portfolio are saved for backtesting.

Task 5: Strategy Backtesting ✅
The 05_backtesting_strategy.ipynb notebook validates the performance of the optimal strategy on a historical period.

Process:

A backtesting period is defined (e.g., the last year of the dataset).

A simple benchmark portfolio (e.g., 60% SPY / 40% BND) is established.

The returns of the optimal strategy are simulated against the benchmark over the backtesting period.

The performance of both portfolios is analyzed by plotting cumulative returns and calculating key metrics like Total Return and the Annualized Sharpe Ratio. The final output includes a conclusion on whether the strategy outperformed the benchmark.