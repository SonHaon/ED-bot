import datetime

def date():
    today=datetime.date.today()
    class date:
        day=today.day
        month=today.month
        year=today.year

        if day < 10:
            day="0"+str(day)
        if month < 10:
            month="0"+str(month)
    
    return date