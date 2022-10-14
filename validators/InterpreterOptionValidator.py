from validators.ValidatorInterface import ValidatorInterface


class InterpreterOptionValidator(ValidatorInterface):

    def validate(self, interpreter_option: int) -> bool:
        return interpreter_option in [1, 2, 3]

    def get_error_message_content(self) -> str:
        return 'Invalid option selected. Try again'
