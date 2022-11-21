import db_statement
import jira_methods
import time
import logging
from datetime import datetime

logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)
errors = (db_statement.geterrors())
for x in errors:
    id_db = str(x[0])
    component = x[2]
    error_name = x[3]
    logging.info(datetime.now().strftime("%d_%m_%Y_:%H:%M:%S") + ' ' + str(x) + '\n')
    id_jira = jira_methods.create_task(id_db+' '+component+' '+error_name, component)
    db_statement.seterrors(id_db, id_jira)
    time.sleep(2)
