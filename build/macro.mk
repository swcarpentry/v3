INPUT_DIR = /lab/gamma2100
OUTPUT_DIR = /tmp

all : ${OUTPUT_DIR}/hydroxyl_all.csv ${OUTPUT_DIR}/methyl_all.csv

${OUTPUT_DIR}/%_all.csv : ${OUTPUT_DIR}/%_422.csv ${OUTPUT_DIR}/%_480.csv
	@summarize $^ > $@

${OUTPUT_DIR}/%.csv : ${INPUT_DIR}/%.dat
	@dat2csv $< > $@

clean :
	@rm -f *.csv
