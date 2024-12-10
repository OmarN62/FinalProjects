import calendar

def creatingCalendar(year, month):

    cal = calendar.monthcalendar(year, month)

    print(calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    for week in cal: 
        week_str = " ".join(f"{day:2}" if day else " " for day in week)
        print(week_str)

if __name__ == "__main__":
    year = int(input("Enter year:"))
    month = int(input("Enter month in range of 1 - 12: "))
    creatingCalendar(year, month)