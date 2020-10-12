import interface


def run():
    Main = interface.Interface("Password Generator", (400, 500))
    Main.run()


if __name__ == "__main__":
    run()