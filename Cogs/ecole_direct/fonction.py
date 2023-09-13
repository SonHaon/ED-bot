import datetime

def date(day=datetime.date.today().day,month=datetime.date.today().month):
    today=datetime.date.today()
    
    class date:
        year=today.year
    date.day=day
    date.month=month
    if date.day < 10:
        date.day="0"+str(day)
    if date.month < 10:
        date.month="0"+str(month)
    
    return date