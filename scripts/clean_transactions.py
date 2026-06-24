import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Original Shape:", df.shape)

# Amount should be positive
df = df[df["amount_inr"] > 0]

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

print("Cleaned Shape:", df.shape)

df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Saved successfully.")