SELECT DISTINCT Person.Login
FROM            Person INNER JOIN Involved
WHERE           (ProjectId = 1214) AND (ProjectId = 1709);
