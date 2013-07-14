SELECT DISTINCT A.Login, B.Login
FROM            Involved A CROSS JOIN Involved B
WHERE           (A.ProjectId = B.ProjectId)
AND             (A.ExperimentId = B.ExperimentId)
AND             (A.Login != B.Login);
