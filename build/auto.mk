all : hydroxyl_422.csv methyl_422.csv

hydroxyl_422.csv : hydroxyl_422.dat
	@dat2csv $< > $@

methyl_422.csv : methyl_422.dat
	@dat2csv $< > $@

clean :
	@rm -f *.csv
