SELECT SUM(Experiment.Hours)
FROM   Involved INNER JOIN Experiment
WHERE  (Involved.Login = "mlom")
  AND  (Involved.ProjectId = 1214)
  AND  (Involved.ProjectId = Experiment.ProjectId)
  AND  (Involved.ExperimentId = Experiment.ExperimentId);
