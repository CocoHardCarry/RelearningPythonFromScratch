from datetime import date
import inflect
import sys


def main():
    birth = input("Date of Birth: ")

    try:
        birth_date = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")

    minutes = (date.today() - birth_date).days * 24 * 60

    p = inflect.engine()
    words = p.number_to_words(minutes)
    words = words.replace(" and ", " ")

    print(words.capitalize() + " minutes")


def minutes_since_birth(birth_date):
    birth = date.fromisoformat(birth_date)
    return (date.today() - birth).days * 24 * 60


if __name__ == "__main__":
    main()