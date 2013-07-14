all : hydroxyl_422.csv methyl_422.csv

hydroxyl_422.csv : hydroxyl_422.dat
	dat2csv hydroxyl_422.dat > hydroxyl_422.csv

methyl_422.csv : methyl_422.dat
	dat2csv methyl_422.dat > methyl_422.csv
