-- procedure computes and stores the average
-- score for a student
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser (
  IN user_id INT
)
BEGIN
  -- average_score is a decimal# w/ 5 significant digits and
  -- 2 to the right of the decimal point
  DECLARE avg_score DECIMAL(5, 2)
  SELECT AVG(score) INTO avg_score
  FROM corrections
  WHERE corrections.user_id = user_id

  UPDATE users
  SET average_score = average_score
  WHERE id = user_id;
END //