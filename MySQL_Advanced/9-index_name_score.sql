-- creates index on the table names and the first letter of score

-- create index without adding column and do it in the same line
-- (composite index)

CREATE INDEX idx_name_first_score ON names (name(1), score);