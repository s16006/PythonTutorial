while True:
    try:
        x = int(input('整数を入れてください:'))
        break
    except (TypeError, NameError, ValueError):
        print("数字じゃないじゃん")
