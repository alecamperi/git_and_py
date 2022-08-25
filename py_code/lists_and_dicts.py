def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"ASD": "Facundo", "lastname": "García"}

    super_list = [
        {"firstname": "Facundo", "lastname": "García"},
        my_dict,
        {"firstname": "Pablo", "lastname": "Trinidad"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "Fernandez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 3, 0, 1],
        "floating_nums": [1.1, 4.55, 6.43],
        "mi_lista": my_list,
    }

    for key, value in super_dict.items():
        print(key, ">", value)

    # for i in range(len(super_list)):
    #     print(super_list[i])


if __name__ == '__main__':
    run()