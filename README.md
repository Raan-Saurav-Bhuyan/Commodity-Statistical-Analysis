# 📊 Commodity-Statistical-Analysis: Oil vs. Gold vs. Exchange Rates & Inflation

This repository contains a comprehensive Python-based econometric pipeline for the empirical statistical analysis of the relationship between international Gold and Oil prices, and their multi-dimensional impact on the Indian market, the USD/INR exchange rate, and domestic/international inflation.

## 🎯 Objectives
To investigate the bidirectional relationship, volatility spillovers, long-run co-movements, and temporal causality between energy markets (🛢️ Oil), precious metals (🥇 Gold), foreign exchange (💵 USD/INR), and macroeconomic indicators (📈 Inflation).

## ⚙️ Econometric Pipeline & Modules
The project is structured into a modular, sequential pipeline orchestrated by a central execution script (`main.py`). The pipeline executes the following stages:

### 1️⃣ Preparation (`Preparation/`) 🧹
- **Data Ingestion:** Loads raw datasets spanning prices, CPI, and Exchange Rates.
- **Transformations:** Constructs log prices, log returns, and real (inflation-adjusted) metrics.
- **Synchronization:** Merges diverse frequencies (monthly, yearly) into synchronized analytical views.

### 2️⃣ Stationarity Analysis (`Stationarity/`) 📉
- Performs unit root tests (e.g., ADF, Phillips-Perron) to classify the order of integration ($I(0)$ or $I(1)$) for each time-series variable.
- Ensures proper downstream modeling assumptions are met.

### 3️⃣ Cointegration Tests (`Cointegration/`) 🔗
- Executes the **Johansen Cointegration Test** to identify long-run equilibrium relationships.
- Evaluates multiple distinct variable systems independently: *Nominal*, *Real*, and *Inflation-Augmented*.

### 4️⃣ VECM / VAR Modeling (`vecm_var/`) 🧮
- Dynamically selects optimal lag lengths based on information criteria.
- Fits **Vector Error Correction Models (VECM)** for cointegrated systems or **Vector Autoregression (VAR)** for non-cointegrated stationary systems.
- Computes and extracts **Impulse Response Functions (IRF)** and Forecast Error Variance Decompositions (FEVD).

### 5️⃣ Volatility Spillovers (`Volatility/`) 🌪️
- Implements **DCC-GARCH** (Dynamic Conditional Correlation) models.
- Fits individual GARCH models to extract conditional volatilities and computes pairwise dynamic correlations over time to understand shock transmissions.

### 6️⃣ Causality Testing (`Causality/`) 🔀
- Evaluates predictive relationships using rolling-window **Pairwise Granger Causality**.
- Conducts **Block Exogeneity** (VAR-based) tests to capture structural shifts in causal dynamics over time.

### 7️⃣ Reporting & Visualization (`Reporting/`) 📑
- Automatically collects serialized results, summary tables, and text reports.
- Generates rich diagnostic visualizations including:
  - Granger Causality Heatmaps
  - Dynamic Conditional Correlation (DCC) line charts
  - VECM Adjustment Coefficient (Alpha/Beta) significance bar plots

## 🚀 How to Run
Execute the entire pipeline sequentially from the root directory:
```bash
python main.py
```

## 📁 Repository Structure
- `main.py`: The primary pipeline execution runner.
- `Datasets/`: Contains raw CSV files and processed, structured data representations.
- `Results/`: Output directory for serialized model objects (`.pkl`, `.npy`), tables (`.csv`), textual model summaries, and generated high-quality figures.
