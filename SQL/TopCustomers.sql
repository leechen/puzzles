-- The company wants to identify the top 10% of customers who are responsible for the highest total revenue.
--  How would you approach this problem, and what metrics would you use to determine the top 10% of customers?

SELECT customer_id, 
       SUM(quantity * price) AS total_revenue
FROM purchases
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT (SELECT COUNT(DISTINCT customer_id) * 0.1 FROM purchases);