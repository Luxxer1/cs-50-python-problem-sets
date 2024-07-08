from random import randrange


def main():
    score = 0
    eee = 0
    level = get_level()
    for i in range(10):
        x, y = generate_integer(level)
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    eee += 1
                    if eee >= 3:
                        print(f"{x} + {y} = {x + y}")
                        break
            except ValueError:
                pass
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1 or level > 3:
                pass
            else:
                break
        except ValueError:
            pass

    return level


def generate_integer(level):
    match level:
        case 1:
            x = randrange(0, 10)
            y = randrange(0, 10)
            return x, y
        case 2:
            x = randrange(10, 100)
            y = randrange(10, 100)
            return x, y
        case 3:
            x = randrange(100, 1000)
            y = randrange(100, 1000)
            return x, y


if __name__ == "__main__":
    main()
