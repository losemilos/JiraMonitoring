import oracle_config
import oracledb

con = oracledb.connect(user=oracle_config.user, password=oracle_config.password, dsn=oracle_config.dsn)
cur = con.cursor()


def geterrors():
    cur.execute("SELECT * FROM STORE.FOM_ERRORS fe WHERE STATUS_ERROR ='NEW' AND DESCRIPTION IS NULL")
    rows = cur.fetchall()
    return rows


def seterrors(id_error, id_jira):
    statment = "UPDATE STORE.FOM_ERRORS fe SET DESCRIPTION = :v WHERE ERROR_ID = :n"
    cur.execute(statment, {'v': id_jira, 'n': id_error})
    con.commit()
