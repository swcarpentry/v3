SELECT   Involved.Login, SUM(Experiment.Hours)
FROM     Involved INNER JOIN Experiment
WHERE    (Involved.ProjectId = Experiment.ProjectId)
  AND    (Involved.ExperimentId = Experiment.ExperimentId)
GROUP BY Involved.Login;
