SELECT Experiment.ProjectId, Experiment.ExperimentId, Experiment.Hours
FROM Experiment
WHERE Experiment.Hours < 0;
