-- creates a stored procedure AddBonus that adds a new
-- correction for a student

DELIMITER $$
CREATE PROCEDURE AddBonus (
  IN user_id INT,
  IN project_name VARCHAR(255),
  IN score INT
)

BEGIN
  DECLARE project_id INT;
  -- checl whether project exists
  SELECT id INTO project_id
  FROM projects
  WHERE name = project_name

  -- if no project then create it
  IF project_id IS NULL THEN
    INSERT INTO projects (name) VALUES (project_name)
    -- LAST_INSERT_ID() returns the last automatically generated value set for
    -- an AUTO_INCREMENT column during the most recent INSERT operation
    SET project_id = LAST_INSERT_ID();
  END IF;

  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, project_id, score);
END $$

DELIMITER ;
