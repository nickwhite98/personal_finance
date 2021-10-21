import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    '''Create a connection to the sqlite database'''

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)

    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    '''
    create a table from the passed in create_table_sql statement
    conn param: connection object
    create_Table_sql: a CREATE TABLE SQL statement
    '''
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    conn = create_connection("finance.db")

    create_balance_table = """CREATE TABLE IF NOT EXISTS balances(
                                    id integer PRIMARY KEY,
                                    amount real,
                                    last_updated text 
                                    );
                                    """
    
    create_transactions_table = """CREATE TABLE IF NOT EXISTS transactions(
                                    id integer PRIMARY KEY,
                                    type text,
                                    amount real,
                                    date text,
                                    category text,
                                    balance_id integer NOT NULL,
                                    FOREIGN KEY (balance_id) REFERENCES balances (id)
                                    );
                                    """
    
    if conn is not None:
        create_table(conn, create_balance_table)
        create_table(conn, create_transactions_table)

    else:
        print("No db connection")
