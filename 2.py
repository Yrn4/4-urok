def bread(func):
    def wrapper():
        print()
        func()
        print("<\_____/>")
        return wrapper
def ingredients(func):
    def wrapper ():
        print("#помидоры")
        func()
        print("~салат~")
    return wrapper
def sandwich (food = "--ветчина--"):
    print (food)
sandwich = bread(ingredients(sandwich))
sandwich()
    