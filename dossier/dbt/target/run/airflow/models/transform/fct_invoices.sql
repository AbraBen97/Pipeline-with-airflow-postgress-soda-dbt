
  
    

  create  table "airflow"."public"."fct_invoices__dbt_tmp"
  
  
    as
  
  (
    -- fct_invoices.sql

-- Create the fact table by joining the relevant keys from dimension table
WITH fct_invoices_cte AS (
    SELECT
        invoiceno AS invoice_id,
        invoicedate AS datetime_id,
        md5(cast(coalesce(cast(stockcode as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(description as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(unitprice as TEXT), '_dbt_utils_surrogate_key_null_') as TEXT)) as product_id,
        md5(cast(coalesce(cast(customerid as TEXT), '_dbt_utils_surrogate_key_null_') || '-' || coalesce(cast(country as TEXT), '_dbt_utils_surrogate_key_null_') as TEXT)) as customer_id,
        quantity AS quantity,
        quantity * unitprice AS total
    FROM products
    WHERE quantity > 0
)
SELECT
    fi.invoice_id,
    dt.datetime_id,
    dp.product_id,
    dc.customer_id,
    fi.quantity,
    fi.total
FROM fct_invoices_cte fi
INNER JOIN "airflow"."public"."dim_datetime" dt ON fi.datetime_id = dt.datetime_id
INNER JOIN "airflow"."public"."dim_product" dp ON fi.product_id = dp.product_id
INNER JOIN "airflow"."public"."dim_customer" dc ON fi.customer_id = dc.customer_id
  );
  