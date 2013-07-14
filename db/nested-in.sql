SELECT DISTINCT Login
FROM            Involved
WHERE Login NOT IN
  (SELECT DISTINCT Login
   FROM            Involved
   WHERE           Involved.ProjectId = 1737);
