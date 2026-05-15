select name from SalesPerson
where sales_id not in(
    select sales_id from Orders
    where com_id = (select com_id from Company where name = "RED")
);

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna