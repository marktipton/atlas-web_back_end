-- creates index on the table names and the first letter of name

-- create index without adding column
CREATE INDEX idx_name_first ON names (name(1));

