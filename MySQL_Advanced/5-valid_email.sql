-- Trigger reset attributes when email is changed

CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW

  IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;

