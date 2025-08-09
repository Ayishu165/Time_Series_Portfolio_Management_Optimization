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