-- creates index on the table names and the first letter of score

-- create index without adding column
CREATE INDEX idx_name_first_score ON names (score);