import os, datetime, pathlib, sqlite3

# # #

ROOT_FOLDER_PATH = pathlib.Path(__file__).parent.parent.absolute()
DATABASE_PATH = ROOT_FOLDER_PATH / "databases"
DATABASE_NAME = "serverHistory.db"

# # #

INITIAL_CALLS_TABLE = [
    # # #
    """CREATE TABLE IF NOT EXISTS USER_REGISTER (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	JOIN_DATE DATETIME NOT NULL,
	USERNAME TEXT(32) COLLATE NOCASE NOT NULL
    );""",
    # # #
    """CREATE TABLE IF NOT EXISTS USER_ACTIVITY (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	ACTION_DATE DATETIME NOT NULL,
	USERNAME TEXT(32) COLLATE NOCASE NOT NULL,
	ACTION_NAME TEXT(32) COLLATE NOCASE NOT NULL,
    ACTION_EXTRA TEXT(128) COLLATE NOCASE
    );"""
    # # #
]

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
            for query in INITIAL_CALLS_TABLE:
                self.databaseCursor.execute(query, [])
            self.databaseConn.commit()
            print("{} OK".format(DATABASE_NAME))
        except sqlite3.Error as error:
            print("Error while working with SQLite: ", error)

    def __del__(self):
        self.databaseCursor.close() if self.databaseConn else None
        self.databaseConn.close() if self.databaseConn else None
        pass

    def AddRegisterRecord(self, userName: str):
        SQL_COMMAND = "INSERT INTO USER_REGISTER (JOIN_DATE, USERNAME) VALUES (?, ?);"
        try:
            timestamp = datetime.datetime.utcnow()
            self.databaseCursor.execute(SQL_COMMAND, (timestamp, userName))
            self.databaseCursor.fetchall()
            self.databaseConn.commit()
            print("execute AddRegisterRecord OK")
        except sqlite3.Error as error:
            print("Error while working with SQLite: ", error)

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