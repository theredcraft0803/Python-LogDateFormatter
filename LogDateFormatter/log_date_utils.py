from datetime import datetime

class LogDateUtils:
    @staticmethod
    def getLogDateFormat(date: datetime = None) -> str:
        if date is None:
            date = datetime.now()
        return date.strftime("[%d-%m-%Y %H:%M:%S]")
