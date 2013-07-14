SELECT Project.ProjectName, Experiment.ExperimentId, Experiment.Hours
FROM Project INNER JOIN Experiment
WHERE (Project.ProjectId = Experiment.ProjectId)
  AND (Experiment.Hours < 0);
