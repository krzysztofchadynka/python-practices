import pandas as pd


class DataImporter:
    def __init__(self, file_format: str, file_path: str):
        self.file_format = file_format
        self.file_path = file_path

    def import_file(self) -> pd.DataFrame:
        return self.__import_file_by_extension()

    # TODO: Replace it with mach function after update to python 3.10
    def __import_file_by_extension(self) -> pd.DataFrame:
        if self.file_format == 'c':
            return pd.read_csv(self.file_path)
        elif self.file_format == 'j':
            return pd.read_json(self.file_path)
        elif self.file_format == 'x':
            return pd.read_xml(self.file_path)
        elif self.file_format == 'p':
            return pd.read_parquet(self.file_path, engine='pyarrow')

        print('Given file extension not supported.')
        pass
