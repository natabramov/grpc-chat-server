import sqlite3
from sqlite3 import Error
#from chat_server import Account_Create


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def alter_table(conn, alter_table_sql):
    try:
        c = conn.cursor()
        c.execute(alter_table_sql)
    except Error as e:
        print(e)    

def create_cred(conn, cred):
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

def create_channel_owner(conn, cred):
    sql = ''' INSERT INTO channel_owners 
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, cred)
    conn.commit()

def delete_channel_owner(conn, cred):
    sql = ''' DELETE FROM channel_owners WHERE channel = \"''' + str(cred[0]) + "\""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def read_channel_owner(conn, cred):
    sql = ''' SELECT * FROM channel_owners WHERE channel = \"''' + str(cred[0]) + "\""
    cur = conn.cursor()
    cur.execute(sql)
    #conn.commit()
    return cur.fetchall()

def add_account_status(conn, cred):
    sql = ''' INSERT INTO account_status 
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, cred)
    conn.commit()

def update_account_status(conn, cred):
    sql = f"UPDATE account_status SET status = {int(cred[1])} WHERE username = '{str(cred[0])}'"
    cur = conn.cursor()
    cur.execute(sql, cred)
    conn.commit()

def read_status(conn, cred):
    sql = ''' SELECT * FROM acc WHERE username = \"''' + str(cred[0]) + "\""
    cur = conn.cursor()
    cur.execute(sql)
    #conn.commit()
    return cur.fetchall()

def delete_account_status(conn, cred):
    sql = ''' DELETE FROM account_status WHERE username = \"''' + str(cred[0]) + "\""
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def main():
    database = r"C:\Users\Natalie\summer-project\chat-server\summer-project\sqlite\db\pythonsqlite2.db"

    sql_create_status_table = ''' CREATE TABLE IF NOT EXISTS account_status (
                                    username text NOT NULL,
                                    status integer,
                                    UNIQUE (username)
                                ); '''


    sql_del_table = ''' DROP TABLE account_status; '''

    # create a database connection
    conn = create_connection(database)

    # with conn:
    #     cred = ('testchannel', 'natabr')
        #create_channel_owner(conn, cred)
        #print(read_cred(conn,cred))
        # print(read_channel_owner(conn, cred))
        # delete_cred(conn, cred)
        # delete_channel_owner(conn, cred)
        # print(read_channel_owner(conn, cred))
        # cred = ('testchannel', 'natabr', '')
        # print(read_channel_owner(conn, cred))

        # cred2 = ('fattykitty3', 'kiwi55!')
        #create_cred(conn, cred)
        # print(read_cred(conn, cred2))
        #delete_cred(conn, cred2)


    # create tables
    if conn is not None:
        #create projects table
        create_table(conn, sql_create_status_table)

    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
    main()