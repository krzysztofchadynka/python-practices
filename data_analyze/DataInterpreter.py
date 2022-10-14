import pandas as pd


class DataInterpreter:
    def __init__(self, date_frame: pd.DataFrame):
        self.data_frame = date_frame

    def get_single_column_values(
            self,
            column_name: str,
            first_position: int = None,
            last_position: int = None
    ) -> pd.Series:
        if not (first_position or last_position):
            return self.data_frame.loc[:, column_name]
        if first_position and not last_position:
            return self.data_frame.loc[first_position:, column_name]
        if last_position and not first_position:
            return self.data_frame.loc[:last_position, column_name]
        if first_position and last_position:
            return self.data_frame.loc[first_position:last_position, column_name]

    def get_records(self, limit: int = None, selected_indexes: list = None) -> pd.DataFrame:
        if limit:
            if limit >= 0:
                return self.data_frame.iloc[:limit:]
            else:
                return self.data_frame.iloc[limit:]

        if selected_indexes:
            return self.data_frame.loc[selected_indexes, :]

        return self.data_frame

    def get_many_columns(self, column_names: list) -> pd.DataFrame:
        return self.data_frame.loc[:, column_names]
