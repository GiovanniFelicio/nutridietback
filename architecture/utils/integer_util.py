import re


class IntegerUtil:

    @staticmethod
    def only_numbers(string: str) -> str:
        return re.sub('[^0-9]', '', string)
