
  
    

  create  table "airflow"."public"."dim_product__dbt_tmp"
  
  
    as
  
  (
    -- dim_product.sql
-- StockCode isn't unique, a product with the same id can have different and prices
-- Create the dimension table
SELECT DISTINCT
    md5(cast(coalesce(cast(stockcode as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(description as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(unitprice as TEXT), '_dbt_utils_surrogate_key_null_') as TEXT)) as product_id,
		stockcode AS stock_code,
    description AS description,
    unitprice AS price
FROM products
WHERE stockcode IS NOT NULL
AND unitprice > 0
  );
  