INPUT_DIR = /lab/gamma2100
OUTPUT_DIR = /tmp
CHEMICALS = hydroxyl methyl
SUMMARIES = $(addprefix ${OUTPUT_DIR}/,$(addsuffix _all.csv,${CHEMICALS}))

all : ${SUMMARIES}

${OUTPUT_DIR}/%_all.csv : ${OUTPUT_DIR}/%_422.csv ${OUTPUT_DIR}/%_480.csv
	@summarize $^ > $@

${OUTPUT_DIR}/%.csv : ${INPUT_DIR}/%.dat
	@dat2csv $< > $@

clean :
	@rm -f *.csv
