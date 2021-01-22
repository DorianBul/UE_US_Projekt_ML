import os, datetime, pathlib, sqlite3

# # #

ROOT_FOLDER_PATH = pathlib.Path(__file__).parent.parent.absolute()
DATABASE_PATH = ROOT_FOLDER_PATH / "databases"
DATABASE_NAME = "serverHistory.db"

# # #

class DatabaseManager:
    # # #
    DATABASE_FILE = DATABASE_PATH / DATABASE_NAME
    # # #
    databaseConn = None
    databaseCursor = None
    # # #

    def __init__(self):
        try:
            self.databaseConn = sqlite3.connect(self.DATABASE_FILE, check_same_thread=False)
            self.databaseCursor = self.databaseConn.cursor()
            print("{} OK".format(DATABASE_NAME))
        except sqlite3.Error as error:
            print("Error while working with SQLite: ", error)

    def __del__(self):
        self.databaseCursor.close() if self.databaseConn else None
        self.databaseConn.close() if self.databaseConn else None
        pass


    def AddActionRecord(self, userName: str, actionName: str, actionExtra: str):
        SQL_COMMAND = "INSERT INTO USER_ACTIVITY (ACTION_DATE, USERNAME, ACTION_NAME, ACTION_EXTRA) VALUES (?, ?, ?, ?);"
        try:
            timestamp = datetime.datetime.utcnow()
            self.databaseCursor.execute(SQL_COMMAND, (timestamp, userName, actionName, actionExtra))
            self.databaseCursor.fetchall()
            self.databaseConn.commit()
            print("execute AddActionRecord OK")
        except sqlite3.Error as error:
            print("Error while working with SQLite: ", error)

# # #

dbManager = DatabaseManager()

# # #