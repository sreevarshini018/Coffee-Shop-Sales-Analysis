-- Total Sales

SELECT SUM(money)
FROM coffee_sales;

-- Average Sale

SELECT AVG(money)
FROM coffee_sales;

-- Top Selling Coffee

SELECT coffee_name,
SUM(money) TotalSales
FROM coffee_sales
GROUP BY coffee_name
ORDER BY TotalSales DESC;

-- Payment Method

SELECT cash_type,
COUNT(*)
FROM coffee_sales
GROUP BY cash_type;

-- Daily Sales

SELECT date,
SUM(money)
FROM coffee_sales
GROUP BY date
ORDER BY date;