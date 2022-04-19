time = int(input("duration "))
if time < 60:
    print(f"{time} сек")
if time >= 60 and time < 3600:
    print(time // 60, "мин", time % 60, "сек")
if time >= 3600 and time < 86400:
    print(time // 3600, "час", time % 3600 // 60, "мин", time % 60, "сек")
if 86400 <= time:
    print(time // 86400, "дн", time % 86400 // 3600, "час", time % 3600 // 60, "мин", time % 60, "сек")

