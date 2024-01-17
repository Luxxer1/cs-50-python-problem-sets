def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if not time.endswith("a.m.") | time.endswith("p.m."):
        hours, minutes = time.split(":")
        time = int(hours) + float(minutes) / 60
    else:
        real_time, time_cicle = time.split(" ")
        if time_cicle == "p.m.":
            hours, minutes = real_time.split(":")
            time = (int(hours) + 12) + float(minutes) / 60
        else:
            hours, minutes = real_time.split(":")
            time = int(hours) + float(minutes) / 60
    return time

if __name__ == "__main__":
    main()
