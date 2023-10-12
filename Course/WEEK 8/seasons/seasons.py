from datetime import date, datetime, timedelta
import inflect
import sys

def main():
    try:
        birth_date = datetime.strptime(input("Date of birth: "), '%Y-%m-%d')
    except:
        raise sys.exit('Invalid date')
    p = inflect.engine()
    today = datetime.strptime("2000-01-01", "%Y-%m-%d")
    check_birthday(birth_date)
    time_lapse = today - birth_date
    minutes = time_lapse / timedelta(minutes=1)
    minutes = int(minutes)
    output = p.number_to_words(minutes, andword="")
    output = output.capitalize() + " minutes"
    print(output)

def check_birthday(birth_date):
    try:
        birth_date = birth_date
    except:
        raise sys.exit('Invalid date')
    return True

if __name__ == "__main__":
    main()