SELECT DISTINCT Login
FROM            Involved
WHERE Login NOT IN
  (SELECT DISTINCT A.Login
   FROM Involved A INNER JOIN Involved B
   WHERE (A.Login = B.Login)
   AND   (A.ProjectId != B.ProjectId));
