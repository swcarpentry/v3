all : hydroxyl_422.csv methyl_422.csv

%.csv : %.dat
	@dat2csv $< > $@

clean :
	@rm -f *.csv
