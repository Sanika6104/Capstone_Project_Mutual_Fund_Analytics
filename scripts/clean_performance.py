import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print("Original Shape:", df.shape)

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Convert expense ratio
df["expense_ratio_pct"] = pd.to_numeric(
    df["expense_ratio_pct"],
    errors="coerce"
)

# Remove rows with missing returns
df = df.dropna(
    subset=["return_1yr_pct", "return_3yr_pct", "return_5yr_pct"]
)

# Flag unusual expense ratios
anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("Expense Ratio Anomalies:")
print(anomalies.shape[0])

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Saved scheme_performance_clean.csv")