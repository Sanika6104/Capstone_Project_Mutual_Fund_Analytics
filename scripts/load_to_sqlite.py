import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///bluestock_mf.db")

# Load cleaned files
nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

# Write tables
nav.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

print("SQLite database created successfully!")