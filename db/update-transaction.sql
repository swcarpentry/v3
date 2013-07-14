BEGIN TRANSACTION;

  UPDATE Person
  SET    Login = "kovalev"
  WHERE  Login = "skol";

  UPDATE Involved
  SET    Login = "kovalev"
  WHERE  Login = "skol";

END TRANSACTION;

SELECT *
FROM   Person
WHERE  (Login = "kovalev") OR (Login = "skol");

SELECT *
FROM   Involved
WHERE  (Login = "kovalev") OR (Login = "skol");
