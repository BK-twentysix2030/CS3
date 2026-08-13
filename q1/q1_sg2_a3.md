while True:
    try:
        year = int(input("Enter your birth year: "))
        break
    except ValueError:
        print("Invalid input, run the program again.")
def zodiac(year):
    zodiac = "blank"
    x = year - 1900
    if x % 12 == 0:
        zod = ("Rat (鼠 / Shǔ)")
    elif x % 12 == 1:
        zod = ("Ox (牛 / Niú)")
    elif x % 12 == 2:
        zod = ("Tiger (虎 / Hǔ)")
    elif x % 12 == 3:
        zod = ("Rabbit (兔 / Tù)")
    elif x % 12 == 4:
        zod = ("Dragon (龙 / Lóng)")
    elif x % 12 == 5:
        zod = ("Snake (蛇 / Shé)")
    elif x % 12 == 6:
        zod = ("Horse (马 / Mǎ)")
    elif x % 12 == 7:
        zod = ("Goat (羊 / Yáng)")
    elif x % 12 == 8:
        zod = ("Monkey (猴 / Hóu)")
    elif x % 12 == 9:
        zod = ("Rooster (鸡 / Jī)")
    elif x % 12 == 10:
        zod = ("Dog (狗 / Gǒu)")
    else:
        zod = ("Pig (猪 / Zhū)")
    return zod


if year < 1900:
    print("Invalid year, year must not be earlier than 1900")
else:
    zodiac(year)
    print(f"Your Chinese Zodiac Sign is : {zodiac(year)}")

