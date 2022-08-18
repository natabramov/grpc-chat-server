import sqlite3
from sqlite3 import Error
#from chat_server import Account_Create


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_cred(conn, cred):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO credentials 
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, cred)
    conn.commit()
    return print(cur.fetchall())

def delete_cred(conn, cred):
    sql = ''' DELETE FROM credentials WHERE username = \"''' + str(cred[0]) + "\""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def read_cred(conn, cred):
    sql = ''' SELECT * FROM credentials WHERE username = \"''' + str(cred[0]) + "\""
    cur = conn.cursor()
    cur.execute(sql)
    #conn.commit()
    return cur.fetchall()

def main():
    database = r"C:\Users\Natalie\summer-project\chat-server\summer-project\sqlite\db\pythonsqlite2.db"

    sql_create_cred_table = ''' CREATE TABLE IF NOT EXISTS credentials (
                                    username text NOT NULL,
                                    password text NOT NULL,
                                    UNIQUE(username)
                                ); '''

    # create a database connection
    conn = create_connection(database)

    with conn:
        # create a new project
        cred = ('fatcat', 'kiwi55!')
        #create_cred(conn, cred)
        print(read_cred(conn,cred))
        #print(read_cred(conn, cred)[0])
        #delete_cred(conn, cred)

        #cred2 = ('natabr2', 'hello123')
        #create_cred(conn, cred)
        #delete_cred(conn, cred2)

    # # # create tables
    # if conn is not None:
    #     # create projects table
    #     create_table(conn, sql_create_cred_table)

    # else:
    #     print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()