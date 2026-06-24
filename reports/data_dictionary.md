# Data Dictionary

## fund_master

| Column | Description |
|----------|----------|
| amfi_code | Unique AMFI identifier |
| scheme_name | Mutual fund scheme |
| fund_house | AMC name |
| category | Fund category |
| risk_category | Risk classification |

## nav_history

| Column | Description |
|----------|----------|
| amfi_code | Scheme code |
| date | NAV date |
| nav | Net Asset Value |

## investor_transactions

| Column | Description |
|----------|----------|
| investor_id | Investor ID |
| transaction_date | Transaction date |
| amount_inr | Transaction amount |
| transaction_type | Purchase/Redemption |