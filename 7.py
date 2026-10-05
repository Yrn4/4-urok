class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_valid_age(age):
        return isinstance(age, int) and 0 < age < 150

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str) and len(name) > 0
if  User.is_valid_age(52) and User.is_valid_name("Akakiy"):
    user=User("Akakiy", 52)