from weapon import Weapon


def main():
    stick = Weapon()
    print(stick.name, stick.damage)
    # throws new excetion
    stick.attack(None)


if __name__ == "__main__":
    main()
