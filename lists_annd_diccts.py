
def run():
    my__list = [1, "hello", True, 1.5]
    my_dict = {"firstname": "kevin", "lastname":"corredor"}
    
    supper_list = [
        {"firstname": "kevin", "lastname":"corredor"},
        {"firstname": "aalejandro", "lastname":"ordoñez"},
    ]

    supeer_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1,2,-3],
        "float_numbers": [10.5, 20.5, 32.3]
    }

    for i in supper_list:
         for key, value in i.items():
           print(key, "-", value)


if __name__  == '__main__':
    run()



