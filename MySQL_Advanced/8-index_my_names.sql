-- creates index on the table names and the first letter of name

-- Add column that contains the first letter of the name column
-- using LEFT(name, 1)
ALTER TABLE names
ADD COLUMN first_letter CHAR(1) generated ALWAYS AS (LEFT(name, 1)) STORED;

-- create index on generated column
CREATE INDEX idx_name_first ON names (first_letter);

