-- new view need_meeting that lists students with grade C and lower
-- but only if these students haven't already had a meeting in the last month

CREATE OR REPLACE VIEW need_meeting AS
SELECT
  name
FROM students
WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));
-- query students table to check if meeting has already taken place
SELECT name, score, ISNULL(last_meeting) FROM students;
SELECT * FROM need_meeting;