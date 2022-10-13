from abc import ABC, abstractmethod


class ValidatorInterface(ABC):

    @abstractmethod
    def validate(self, value_to_validate) -> bool:
        pass

    @abstractmethod
    def get_error_message_content(self) -> str:
        pass
