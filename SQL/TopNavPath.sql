/*
Here's another data science interview question:
Question
You're analyzing a dataset of website user behavior, and you want to identify the most common navigation paths that users take. 
The dataset contains the following columns:
user_id (unique identifier for each user)
page_id (unique identifier for each page)
timestamp (timestamp of the page visit)
The dataset is ordered by user_id and timestamp, so you can assume that each row represents a consecutive page visit by the same user.
Task
Write a query or code snippet to extract the top 5 most common navigation paths of length 3 (i.e., 3 consecutive page visits). 
A navigation path is defined as a sequence of 3 page IDs.
Example
If the dataset contains the following rows:
user_id	page_id	timestamp
1	A	1
1	B	2
1	C	3
2	A	4
2	B	5
2	D	6
Then, the navigation path A -> B -> C appears once, and the path A -> B -> D appears once.
*/

WITH navigation_paths AS (
  SELECT 
    user_id,
    CONCAT(page_id, ' -> ', LEAD(page_id) OVER (PARTITION BY user_id ORDER BY timestamp), ' -> ', 
    LEAD(page_id, 2) OVER (PARTITION BY user_id ORDER BY timestamp)) AS path
  FROM 
    website_behavior
)
SELECT 
  path, 
  COUNT(*) AS count
FROM 
  navigation_paths
WHERE 
  path IS NOT NULL  -- exclude rows with NULL values
GROUP BY 
  path
ORDER BY 
  count DESC
LIMIT 5;