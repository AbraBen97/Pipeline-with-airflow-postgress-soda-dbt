-- fct_invoices.sql

-- Create the fact table by joining the relevant keys from dimension table
WITH fct_invoices_cte AS (
    SELECT
        invoiceno AS invoice_id,
        invoicedate AS datetime_id,
        {{ dbt_utils.generate_surrogate_key(['stockcode', 'description', 'unitprice']) }} as product_id,
        {{ dbt_utils.generate_surrogate_key(['customerid', 'country']) }} as customer_id,
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
INNER JOIN {{ ref('dim_datetime') }} dt ON fi.datetime_id = dt.datetime_id
INNER JOIN {{ ref('dim_product') }} dp ON fi.product_id = dp.product_id
INNER JOIN {{ ref('dim_customer') }} dc ON fi.customer_id = dc.customer_id
