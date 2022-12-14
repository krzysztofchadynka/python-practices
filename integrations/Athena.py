from pyathena import connect
import pandas as pd


class Athena:

    def __init__(self, s3_athena_output_dir: str, region_name: str):
        self.cursor = connect(
            s3_staging_dir=s3_athena_output_dir,
            region_name=region_name
        ).cursor()

    def get_databases_list(self) -> pd.DataFrame:
        databases = self.cursor.execute('show databases').fetchall()

        return pd.DataFrame(databases)

    def get_tables_in_database(self, database_name: str) -> pd.DataFrame:
        tables = self.cursor.execute('show tables in ' + database_name).fetchall()

        return pd.DataFrame(tables)

    def get_data_from_selected_table(
            self,
            database_name: str,
            table_name: str,
            limit: int = None
    ):
        sql_parts = ['select * from {}.{} '.format(database_name, table_name)]

        if limit:
            sql_parts.append('limit ' + str(limit))

        data = self.cursor.execute(''.join(sql_parts)).fetchall()

        return pd.DataFrame(data)
