class Phone:
    def call(self):
        print("You can call.")

    def message(self):
        print("You can message.")


class Samsung(Phone):
    # call, message

    def photo(self):
        print("You can take photo.")


# object of phone class
phone = Phone()
phone.call()
phone.message()

# object of samsung class
samsung = Samsung()
samsung.call()
samsung.message()
samsung.photo()

# check subclass
print(issubclass(Samsung, Phone))
print(issubclass(Phone, Samsung))