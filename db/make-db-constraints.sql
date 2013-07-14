-- create:start
CREATE TABLE Person(
	Login		TEXT		NOT NULL,
	LastName	TEXT	        NOT NULL,
	FirstName	TEXT	        NOT NULL,
	PRIMARY KEY (Login)
);
-- create:end

-- insert:start
INSERT INTO Person VALUES("skol",   "Kovalevskaya", "Sofia");
INSERT INTO Person VALUES("mlom",   "Lomonosov",    "Mikhail");
INSERT INTO Person VALUES("dmitri", "Mendeleev",    "Dmitri");
INSERT INTO Person VALUES("ivan",   "Pavlov",       "Ivan");
-- insert:end

CREATE TABLE Project(
	ProjectId	INTEGER		NOT NULL,
	ProjectName	TEXT        	NOT NULL
);

INSERT INTO Project VALUES(1214, "Antigravity");
INSERT INTO Project VALUES(1709, "Teleportation");
INSERT INTO Project VALUES(1737, "Time Travel");

-- experiment:start
CREATE TABLE Experiment(
	ProjectId	INTEGER		NOT NULL,
	ExperimentId	INTEGER		NOT NULL,
	NumInvolved	INTEGER		NOT NULL,
	ExperimentDate	DATE,
	Hours		REAL		NOT NULL
	CONSTRAINT Experiment_Key PRIMARY KEY (ProjectId, ExperimentId)
);
-- experiment:end

INSERT INTO Experiment VALUES(1214, 1, 1, NULL,          1.5);
INSERT INTO Experiment VALUES(1214, 2, 1, "1889-11-01", 14.3);
INSERT INTO Experiment VALUES(1709, 1, 3, "1891-01-22",  7.0);
INSERT INTO Experiment VALUES(1709, 2, 1, "1891-02-23",  7.2);
INSERT INTO Experiment VALUES(1737, 1, 1, "1900-07-05", -1.0);
INSERT INTO Experiment VALUES(1737, 2, 2, "1900-07-05", -1.5);

CREATE TABLE Involved(
	ProjectId	INTEGER		NOT NULL,
	ExperimentId	INTEGER		NOT NULL,
	InvolvedId	INTEGER		NOT NULL,
	Login		TEXT		NOT NULL
);

INSERT INTO Involved VALUES(1214, 1, 1, "mlom");
INSERT INTO Involved VALUES(1214, 2, 1, "mlom");
INSERT INTO Involved VALUES(1709, 1, 1, "dmitri");
INSERT INTO Involved VALUES(1709, 1, 2, "skol");
INSERT INTO Involved VALUES(1709, 1, 3, "ivan");
INSERT INTO Involved VALUES(1709, 2, 1, "mlom");
INSERT INTO Involved VALUES(1737, 1, 1, "skol");
INSERT INTO Involved VALUES(1737, 2, 1, "skol");
INSERT INTO Involved VALUES(1737, 2, 2, "ivan");
