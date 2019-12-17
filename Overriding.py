class Phone:
    def __init__(self):
        print("I am phone class.")


class Samsung(Phone):
    # constructor

    def __init__(self):
        # override super class constructor
        super().__init__()
        print("I am samsung class.")


# object
samsung = Samsung()