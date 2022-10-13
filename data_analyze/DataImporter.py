import pandas as pd


class DataImporter:
    def __init__(self):
        self.sample_dataframe = None

    def create_sample_dataframe(self):
        self.sample_dataframe = pd.DataFrame(self.__get_sample_dataframe_content())

    def get_sample_dataframe(self):
        return self.sample_dataframe

    @staticmethod
    def __get_sample_dataframe_content():
        return [
            {
                'country': 'Poland',
                'continent': 'Europe',
                'points': 1000,
                'description': 'Lorem ipsum',
            },
            {
                'country': 'Germany',
                'continent': 'Europe',
                'points': 700,
                'description': 'Dolor sit amet',
            },
            {
                'country': 'Croatia',
                'continent': 'Europe',
                'points': 700,
                'description': 'Lorem ipsum',
            }
        ]
