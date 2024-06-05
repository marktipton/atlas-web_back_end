-- divides and returns result of two numbers

CREATE FUNCTION SafeDiv(a INT, b INT)
  IF b == 0
    RETURN 0
  ELSE
    RETURN a / b;