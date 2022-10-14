from validators.FileSourceValidator import FileSourceValidator
from validators.FileFormatValidator import FileFormatValidator
from validators.FilePathValidator import FilePathValidator
from data_analyze.DataImporter import DataImporter
import pandas as pd


class UI:
    @staticmethod
    def select_file_source() -> str:
        file_source_validator = FileSourceValidator()

        print('Do you want to import [y]our own or a [s]ample file?')
        file_source = input()

        if not file_source_validator.validate(file_source):
            print(file_source_validator.get_error_message_content())
            exit(0)

        return str(file_source)

    @staticmethod
    def import_sample_file() -> pd.DataFrame:
        return DataImporter('p', 'sample-import-file.parquet').import_file()

    def import_user_file(self):
        file_format = self.__select_file_format()
        file_path = self.__select_file_path()

        return DataImporter(file_format, file_path).import_file()

    @staticmethod
    def __select_file_format() -> str:
        file_format_validator = FileFormatValidator()

        print('File format: [c]sv, [j]son, [x]ml')

        while True:
            file_format = input()

            if not file_format_validator.validate(file_format):
                print(file_format_validator.get_error_message_content())
                continue
            else:
                return file_format

    @staticmethod
    def __select_file_path() -> str:
        file_path_validator = FilePathValidator()

        print('File path:')
        file_path = input()

        if not file_path_validator.validate(file_path):
            print(file_path_validator.get_error_message_content())
            exit(0)

        return file_path
