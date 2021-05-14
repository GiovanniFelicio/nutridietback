import re


class IntegerUtil:

    @staticmethod
    def only_numbers(string: str) -> str:
        only_numbers = re.sub('[^0-9]', '', string)
        return only_numbers
