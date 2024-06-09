-- new view need_meeting that lists students with grade C and lower
-- but only if these students haven't already had a meeting in the last month

CREATE VIEW need_meeting AS
SELECT
  name, score, last_meeting FROM students
  WHERE score < 80
  AND last_meeting = NULL
  OR last_meeting > 1;


SELECT * FROM need_meeting;