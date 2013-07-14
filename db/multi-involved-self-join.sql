SELECT DISTINCT A.Login
FROM            Involved A CROSS JOIN Involved B
WHERE           (A.Login = B.Login)
AND             (A.ProjectId != B.ProjectId);
