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
