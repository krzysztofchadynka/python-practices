from validators.ValidatorInterface import ValidatorInterface


class FileFormatValidator(ValidatorInterface):

    def validate(self, value_to_validate) -> bool:
        return (value_to_validate in 'cjx') and (len(value_to_validate) == 1)

    def get_error_message_content(self) -> str:
        return 'Wrong option selected. Try again.'
