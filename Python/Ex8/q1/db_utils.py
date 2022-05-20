import sqlite3

from bill import Bill


class DBUtils:
    __DATABASE_NAME = 'my_database.db'
    TABLE_NAME = 'bills'

    def __init__(self):
        try:
            self._db = sqlite3.connect(self.__DATABASE_NAME)
            self._cursor = self._db.cursor()
        except Exception as e:
            print(f"Exception while trying to connect DB, {str(e)}")

    def close(self):
        self._db.close()

    def create_table(self, table_name: str = TABLE_NAME):
        self._cursor.execute(f'''
                    CREATE TABLE {table_name}(BillID INTEGER KEY, Name TEXT,
                    KnessetNum INTEGER, StatusID INTEGER, PrivateNumber INTEGER unique, LastUpdatedDate SMALLDATETIME)
                    ''')
        self._db.commit()

    def insert(self, bill: Bill, table_name: str = TABLE_NAME):
        self._cursor.execute(
            f'''INSERT INTO {table_name}(BillID, Name, KnessetNum, StatusID, PrivateNumber, LastUpdatedDate)
                           VALUES(:BillID, :Name, :KnessetNum, :StatusID, :PrivateNumber, :LastUpdatedDate)''',
            bill.convert_to_dict())
        self._db.commit()

    def print_table(self, num_of_rows: int = None, table_name: str = TABLE_NAME):
        self._cursor.execute(f"SELECT * FROM {table_name}")
        if num_of_rows is not None:
            rows = self._cursor.fetchmany(size=num_of_rows)
        else:
            rows = self._cursor.fetchall()
        for row in rows:
            print(f"result: {row}\n")
