from validators.ValidatorInterface import ValidatorInterface


class FileSourceValidator(ValidatorInterface):
    def validate(self, file_source) -> bool:
        return (file_source in 'ys') and (len(file_source) == 1)

    def get_error_message_content(self) -> str:
        return 'Given option not supported. Bye.'
