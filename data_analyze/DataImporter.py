import pandas as pd


class DataImporter:
    def __init__(self, file_format: str, file_path: str):
        self.file_format = file_format
        self.file_path = file_path
