from architecture.exceptions.unprocessable import UnprocessablePatternDate
from architecture.exceptions.unprocessable import UnprocessableDatePeriod


class DateUtil:

    @staticmethod
    def is_date_valid(date: str) -> bool:

        try:
            year, month, day = map(int, date.split('-'))
        except:
            raise UnprocessablePatternDate()

        if month < 1 or month > 12 or year <= 0:
            raise UnprocessableDatePeriod()

        if month in (1, 3, 5, 7, 8, 10, 12):
            last_day = 31
        elif month == 2:
            if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                last_day = 29
            else:
                last_day = 28
        else:
            last_day = 30

        if day < 1 or day > last_day:
            raise UnprocessableDatePeriod()

        return True
