import sqlalchemy
from sqlalchemy import MetaData, Table, create_engine, select
import datetime
import os
import pandas as pd


class Database:
    def __init__(self, database_path: str):
        """Creates a connection to the database.

        Args:
            database_path (str): Path to the database file.
        """
        self.database_path = database_path
        self.engine = sqlalchemy.create_engine("sqlite://///" + database_path)

        self.metadata = MetaData()
        self.table = Table()

        self.last_id = 0

    def get_table_attributes(self, table_name: str):
        """Gets basic table properties and prints them to console.

        Args:
            table_name (str): Table name.
        """
        self._init_table(table_name)
        print("TABLE NAMES:")
        print(self.engine.table_names())
        print("COLUMN NAMES:")
        print(self.table.columns.keys())
        print("TABLE TYPES:")
        print(repr(self.table))

    def select_all(self, table_name: str):
        self._init_table(table_name)
        connection = self.engine.connect()
        querry_res = list(connection.execute(select(self.table)).fetchall())
        connection.close()
        return querry_res

    def select_by_id(self, table_name: str, id):
        self._init_table(table_name)
        connection = self.engine.connect()
        querry_res = list(
            connection.execute(select(self.table).where(self.table.c.id == id))
        )
        connection.close()
        return querry_res

    def get_last_id(self, table_name: str):
        self._init_table(table_name)
        connection = self.engine.connect()
        querry_res = list(
            connection.execute(
                select(self.table).order_by(self.table.c.id.desc()).limit(1)
            )
        )
        connection.close()
        return querry_res[0][0]

    def insert_into(self, table_name: str, values: list):
        """Inserts data into table.

        Args:
            table_name (str): Table name.
            values (list): List of dictionaries with key-value pairs.
        """
        self._init_table(table_name)
        self._exe([self.table.insert(), values])

    def _init_table(self, table_name: str):
        """[PRIVATE] Creates table and metadata.

        Args:
            table_name (str): Table name.
        """
        self.metadata = MetaData()
        self.table = Table(
            table_name, self.metadata, autoload=True, autoload_with=self.engine
        )

    def _exe(self, exe: list):
        connection = self.engine.connect()
        r = connection.execute(*exe)
        self.last_id = r.lastrowid
        connection.close()


def create_route():
    db.insert_into(
        "api_route",
        [
            {
                "date_time": datetime.datetime.now(),
                "created_at": datetime.datetime.now(),
            }
        ],
    )


db_path = "/home/leo/git_repos/github/GPS-visualization-Django-React/route_visalizer_site/db.sqlite3"
db = Database(db_path)


# print(db.engine.table_names())
# db.get_table_attributes("api_route")
# print(db.select_all("api_route"))
# print("==")
# print(db.select_by_id("api_route", 1))
# print(db.get_last_id("api_route"))

data_path = r"./data/preprocessed/"
for file_name in os.listdir(data_path):

    # For debugging
    # print(file_name)
    if file_name.endswith(".pkl"):

        create_route()
        route_id = db.last_id

        file_path = data_path + str(file_name)

        data = pd.read_pickle(file_path)

        data1 = data[["LATITUDE", "LONGITUDE"]]
        data1.columns = ["latitude", "longitude"]
        data1["route_id_id"] = route_id
        data_final = data1.to_dict("records")

        db.insert_into("api_gpsrecord", data_final)

        print()
