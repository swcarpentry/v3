SELECT Project.ProjectName, Involved.Login
FROM   Project, Involved
WHERE  Project.ProjectId = Involved.ProjectId;
