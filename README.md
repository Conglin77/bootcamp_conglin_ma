# Predicting Short-Term Returns of the SSE Composite Index

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
The Chinese A-share market is known for being highly volatile. It is often driven by retail investor sentiment and sudden policy news, making it really hard to predict short-term trends. In this case, many investors lost their money in this market.

The goal of this project is to build a predictive model to estimate the 5-day percentage return of the Shanghai Stock Exchange (SSE) Composite Index. By examining historical prices, trading volume, and some basic technical indicators (like Moving Averages and MACD), I want to know if we can anticipate short-term market momentum.

## Stakeholder & User
- **Primary Stakeholder / User:** A junior portfolio manager at a small fund, or an active individual investor trying to manage their stock exposure.
- **Decision Context:** They would look at the model's prediction at the end of the week or before making a big trade. It helps them decide: "Should I hold my current positions, or is the market looking too risky for the next few days?"

## Useful Answer & Decision
- **Task Type:** Predictive.
- **Target:** The cumulative percentage return of the SSE Index over the next 5 trading days.
- **Metrics to use:** 
  - RMSE (to see how far off our percentage prediction is).
  - Directional Accuracy (did the model correctly guess 'Up' or 'Down'?).
- **Deliverable:** A Python notebook with the trained model and a clear summary of the current market prediction.

## Assumptions & Constraints
- I am assuming that historical price patterns and trading volumes actually contain useful signals for future trends.
- The model must only use data from *before* the prediction day to avoid cheating (no look-ahead bias).
- The Chinese market has long holidays (like the Spring Festival), so the dataset will have missing dates that need to be handled.
- Only select a small set of basic technical indicators rather than a massive, overly complex dataset.

## Known Unknowns / Risks
- The A-share market is heavily influenced by government policies. A sudden news announcement can completely break historical patterns, and my model won't see that coming.
- The model might just overfit to the historical training data and perform poorly on new, unseen data.
- Technical indicators sometimes generate a lot of false signals when the market is just moving sideways.

## Lifecycle Mapping
Goal → Stage → Deliverable
- Define what to predict and who needs it → Problem Framing & Scoping (Stage 01) → This README and a stakeholder memo.
- Set up a clean coding environment → Tooling Setup (Stage 02) → Repo structure and `.env` file.
- Write code to explore the data → Python Fundamentals (Stage 03) → Helper functions in `src/utils.py` and a basic notebook.
- Download historical stock data → Data Acquisition → CSV files in `data/raw/`.
- Clean the data and handle holidays → Data Preprocessing → Cleaned data in `data/processed/`.
- Create technical indicators → Feature Engineering → Ready-to-use dataset for modeling.
- Train the 5-day prediction model → Modeling & Evaluation → Model outputs and accuracy scores.
- Share the results → Reporting & Communication → Final notebook and summary charts.

## Repo Plan
```text
project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── docs/
└── README.md
## Data Storage

This project uses separate folders for raw and processed data.

- `data/raw/` stores raw CSV files.
- `data/processed/` stores processed Parquet files.
- Storage paths are configured using environment variables:
  - `DATA_DIR_RAW`
  - `DATA_DIR_PROCESSED`

The saved files are reloaded and validated by checking:
- DataFrame shape
- Important column data types

CSV is used for raw data because it is simple and widely compatible.
Parquet is used for processed data because it is more efficient and preserves data types well.