def main():
    list = {
    "January" : "1",
    "February" : "2",
    "March" : "3",
    "April" : "4",
    "May" : "5",
    "June" : "6",
    "July" : "7",
    "August" : "8",
    "September" : "9",
    "October" : "10",
    "November" : "11",
    "December" : "12"
    }

    while True:
        try:
            date = input("Date: ").title()

            if "/" in date:
                m, d, y = date.split("/")
                m = int(m)
                d = int(d)

                if m > 12 or d > 31:
                    raise ValueError
                print(f"{y}-{m:02}-{d:02}")

            else:
                m, d, y = date.split(" ")
                d = d.replace(",", "")
                d = int(d)


                if m in list:
                    m = m.replace(m, list[m])
                    m = int(m)
                else:
                    raise ValueError

                if d > 31:
                    raise ValueError

                print(f"{y}-{m:02}-{d:02}")


        except (ValueError, KeyError):
            pass



main()