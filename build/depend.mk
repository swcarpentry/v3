all : hydroxyl_all.csv methyl_all.csv

%_all.csv : %_422.csv %_480.csv
	summarize $^ > $@

%.csv : %.dat dat2csv
	dat2csv $< > $@

clean :
	@rm -f *.csv
