def main():
    time = input("What time is it? ")
    time = convert(time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("")



def convert(time):
     # Challenge
     if time.endswith(" a.m."):
         time = time.replace(" a.m.","")
         hours, minutes = time.split(":")
         hours = float(hours)
         minutes = float(minutes)

         if hours == 12:
             hours = 0

         return hours + minutes/60

     elif time.endswith(" p.m."):
         time = time.replace(" p.m.","")
         hours, minutes = time.split(":")
         hours = float(hours)
         minutes = float(minutes)

         if hours != 12:
             hours = hours + 12

         return hours + minutes / 60


     else:
        hours, minutes = time.split(':')
        hours = float(hours)
        minutes = float(minutes)
        return hours + minutes/60




if __name__ == "__main__":
    main()