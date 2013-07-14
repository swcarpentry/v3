datafile = 'logging_example.out'
user_id = 'hpotter'
machine_name = 'hogwarts012'
villain = 'dmalfoy'
spell_id = 172
curse = 'Confusius'

import logging

# body:start
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%b-%d %H:%M:%S',
                    filename='logging_example.out',
                    filemode='w')

logging.debug('Last file opened: %s', datafile)
logging.info('User %s logged in normally on %s', user_id, machine_name)
logging.warning('%s attempted to log in as %s', villain, user_id)
logging.error('No such spell (spell ID %04d)', spell_id)
logging.critical('Failed to cast %s', curse)
# body:end
