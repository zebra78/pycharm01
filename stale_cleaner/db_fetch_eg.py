from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
from datetime import datetime
import subprocess


def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def connect():
    """ Connect to MySQL database """

    db_config = read_db_config()
    conn = None
    try:
        print('Connecting to MySQL database...')
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print('Connection established.')
        else:
            print('Connection failed.')

    except Error as error:
        print(error)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Connection closed.')


def query_with_fetchall():
    conn = ""
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT subid, status, partner FROM usersubs")
        rows = cursor.fetchall()
        print(type(rows))
        print('Total Row(s):', cursor.rowcount)
        for row in rows:
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchone():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usersubs")

        row = cursor.fetchone()

        while row is not None:
            print(row)
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def iter_row(cursor, size):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def query_with_fetchmany(size: int = 1):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usersubs")
        print('recvd size: ', size)
        for row in iter_row(cursor, size):
            print('inrow_iterrow')
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def stale_fetchmany(cursor, size) -> list:
    while True:
        return cursor.fetchmany(size)


def stale_fetchall() -> list:
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usersubs")
        return cursor.fetchall()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def stale_bp_stype_old(stale_rows: list):
    for row in stale_rows:
        bp_row = 'cancne#' + str(row[0])
        print(bp_row)
    return


def stale_bp_stype_old2(stale_row: tuple, state_file: str):
    with open(state_file, 'w') as f:
        # print('wrote#'+str(stale_row[0]))
        f.write('cancel#'+str(stale_row[0]))


def stale_bp_print(state_file: str):
    with open(state_file, 'r') as f:
        # print('inread')
        print(f.read())


def create_batchprocessor_inputfile(state_file: str, stale_rows: list):

    with open(state_file, 'a') as f:
        f.write('batchstart\n')
        for stale_row in stale_rows:
            # print('wrote#'+str(stale_row[0]))
            f.write('cancel#'+str(stale_row[0]) + '\n')


def prepare_batchprocessor(state_file: str, size: int = 100):
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usersubs")
        while True:
            rows = cursor.fetchmany(size)
            create_batchprocessor_inputfile(state_file, rows)
            if not rows:
                break
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


def run_batchprocessor_old(stale_file: str) -> bool:
    # result = subprocess.run(["pwd"], stderr=subprocess.PIPE, text=True)
    # result = subprocess.run(["ls", "-l", "../resources/"], stderr=subprocess.PIPE, text=True)
    # result = subprocess.run(["cat", "../resources/stale_clean_sh.sh"], stderr=subprocess.PIPE, text=True)
    # result = subprocess.run(["cat", "stale_file"], stderr=subprocess.PIPE, text=True)
    # result = subprocess.run(["/usr/bin/bash", "../resources/stale_cleaner_sh.sh", stale_file],
    #                                                                       stderr=subprocess.PIPE, text=True)
    # return result.stderr
    exit_code = subprocess.call("/home/madhu/PycharmProjects/pythonProject2/resources/stale_clean_sh.sh")
    print(exit_code)


def run_batchprocessor(stale_file: str):
    print('stale_file = ', stale_file)
    exit_code = subprocess.check_call("../resources/stale_clean_sh.sh %s" % stale_file, shell=True)
    print(exit_code)


if __name__ == '__main__':
    file = "stale_bpinput" + datetime.today().isoformat()
    # query_with_fetchall()
    # query_with_fetchone()
    # query_with_fetchmany(2)
    # rows = stale_fetchall()
    # print(rows)
    # for row in rows:
    #     print('inrow')
    #     stale_bp_stype(row, file)
    # stale_bp_stype(rows, file)
    # stale_bp_print(file)
    # print('Begin stale process... file = ', file)
    prepare_batchprocessor(file, 3)
    run_batchprocessor(file)

