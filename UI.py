from validators.FileSourceValidator import FileSourceValidator
from validators.FileFormatValidator import FileFormatValidator
from validators.FilePathValidator import FilePathValidator
from validators.InterpreterOptionValidator import InterpreterOptionValidator
from data_analyze.DataImporter import DataImporter
from data_analyze.DataInterpreter import DataInterpreter
import pandas as pd


# TODO: This class is temporary should be refactored
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

    def interpret_file(self, data_frame: pd.DataFrame):
        data_interpreter = DataInterpreter(data_frame)
        interpreter_option = self.__select_interpreter_option()

        if interpreter_option == 1:
            print(data_interpreter.get_single_column_values(input('Column name: ')))
        elif interpreter_option == 2:
            range_option = self._select_selected_range_option()

            if range_option == 1:
                print(data_interpreter.get_records())
            if range_option == 2:
                print(data_interpreter.get_records(limit=int(input('Limit: '))))
        elif interpreter_option == 3:
            print(data_interpreter.get_column_names())

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

    @staticmethod
    def __select_interpreter_option() -> int:
        print('What do you want to know about your DataFrame?', end='\n')
        print('[1] - Get values from selected column', end='\n')
        print('[2] - Get records from selected range', end='\n')
        print('[3] - Get column names', end='\n')

        interpreter_option_validator = InterpreterOptionValidator()

        while True:
            interpreter_option = int(input())

            if not interpreter_option_validator.validate(interpreter_option):
                print(interpreter_option_validator.get_error_message_content())
            else:
                return interpreter_option

    # TODO: Add and run validator
    @staticmethod
    def _select_selected_range_option() -> int:
        print('[1] All', end='\n')
        print('[2] Selected limit', end='\n')

        return int(input())
