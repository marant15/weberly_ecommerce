SELECT product_id, MAX(name) name, MAX(lower(trim(category))) category, MAX(price) price
FROM {{ source('ecommerce', 'products') }}
WHERE name IS NOT NULL
  AND category IS NOT NULL
  AND price IS NOT NULL
GROUP BY 1 