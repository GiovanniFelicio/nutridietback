import re


class StringUtil(object):

    @staticmethod
    def is_not_none(string: str) -> bool:
        return string is not None

    @staticmethod
    def is_only_string(string: str):
        return re.match('^[0-9a-zA-Z\u00C0-\u017F´]', string)

    @staticmethod
    def is_none_or_empty(string: str):
        if string is None:
            return True
        elif string == '':
            return True

        return False