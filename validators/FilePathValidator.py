from validators.ValidatorInterface import ValidatorInterface
from os.path import exists


class FilePathValidator(ValidatorInterface):

    def validate(self, file_path) -> bool:
        return exists(file_path)

    def get_error_message_content(self) -> str:
        return 'Given file does not exist.'
