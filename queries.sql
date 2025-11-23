USE [BANGGOOD];
GO

-- 1. Average price per price_tier
SELECT price_tier, AVG(price_pkr) AS avg_price_pkr
FROM BanggoodProducts
GROUP BY price_tier
ORDER BY avg_price_pkr DESC;

-- 2. Average rating per price_tier
SELECT price_tier, AVG(rating) AS avg_rating
FROM BanggoodProducts
GROUP BY price_tier
ORDER BY avg_rating DESC;

-- 3. Product count per price_tier
SELECT price_tier, COUNT(*) AS product_count
FROM BanggoodProducts
GROUP BY price_tier
ORDER BY product_count DESC;

-- 4. Top 5 reviewed items per price_tier
SELECT *
FROM (
    SELECT 
        price_tier,
        product_name,
        reviews,
        price_pkr,
        RANK() OVER (PARTITION BY price_tier ORDER BY reviews DESC) AS review_rank
    FROM BanggoodProducts
) ranked
WHERE review_rank <= 5
ORDER BY price_tier, review_rank;

-- 5. Stock availability percentage (proxy: reviews > 0)
SELECT
    price_tier,
    100.0 * SUM(CASE WHEN reviews > 0 THEN 1 ELSE 0 END)/COUNT(*) AS stock_available_percent
FROM BanggoodProducts
GROUP BY price_tier
ORDER BY stock_available_percent DESC;