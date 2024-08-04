SELECT 
    id,
    date,
    product_id,
    amount,
    SUM(amount) OVER (PARTITION BY product_id ORDER BY date) AS cumulative_sum
FROM 
    sales
ORDER BY 
    product_id, date;
