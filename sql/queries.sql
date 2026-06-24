-- 1. Top 10 funds by 5-year return
SELECT scheme_name, return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 2. Average expense ratio
SELECT AVG(expense_ratio_pct)
FROM scheme_performance;

-- 3. Count schemes by fund house
SELECT fund_house, COUNT(*)
FROM scheme_performance
GROUP BY fund_house
ORDER BY COUNT(*) DESC;

-- 4. Highest AUM funds
SELECT scheme_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;

-- 5. Average 1-year return
SELECT AVG(return_1yr_pct)
FROM scheme_performance;

-- 6. Transaction count by type
SELECT transaction_type, COUNT(*)
FROM investor_transactions
GROUP BY transaction_type;

-- 7. Top cities by transactions
SELECT city, COUNT(*)
FROM investor_transactions
GROUP BY city
ORDER BY COUNT(*) DESC
LIMIT 10;

-- 8. Average investment amount
SELECT AVG(amount_inr)
FROM investor_transactions;

-- 9. Risk grade distribution
SELECT risk_grade, COUNT(*)
FROM scheme_performance
GROUP BY risk_grade;

-- 10. Top performing fund houses
SELECT fund_house,
AVG(return_5yr_pct) AS avg_return
FROM scheme_performance
GROUP BY fund_house
ORDER BY avg_return DESC;