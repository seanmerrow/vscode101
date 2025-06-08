def say_hello(name):
    print("Hello, " + name)

def say_day_of_week(date) -> str:
    import datetime
    day_of_week = datetime.datetime.strptime(date, "%Y-%m-%d").strftime("%A")
    return day_of_week

say_hello("VS Code")

import datetime
print(say_day_of_week(datetime.date.today().strftime("%Y-%m-%d")))