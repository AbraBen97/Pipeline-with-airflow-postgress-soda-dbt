
  
    

  create  table "airflow"."public"."dim_customer__dbt_tmp"
  
  
    as
  
  (
    -- dim_customer.sql

-- Create the dimension table
WITH customer_cte AS (
	SELECT DISTINCT
	    md5(cast(coalesce(cast(customerid as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(Country as TEXT), '_dbt_utils_surrogate_key_null_') as TEXT)) as customer_id,
	    Country AS country
	FROM products
	WHERE CustomerID IS NOT NULL
)
SELECT
    t.*,
	cm.iso
FROM customer_cte t
LEFT JOIN country cm ON t.country = cm.nicename
  );
  