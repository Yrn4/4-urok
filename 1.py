def my_shiny_new_decorator(function_to_decorate):
    def the_wrapper_around_the_original_funcrion():
        print ("Я - код, который отрабоатет до вызова функций")
        function_to_decorate()
        print ("А я код, который отрабоатет ПОСЛЕ")
    return the_wrapper_around_the_original_funcrion
def stand_alone_fuction():
    print ("Я просто функция, и я не хочу изменений")
stand_alone_fuction_decorated = my_shiny_new_decorator(stand_alone_fuction)
stand_alone_fuction_decorated()