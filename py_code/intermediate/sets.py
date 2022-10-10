# my_set_1 = {1,4}
# my_set_2 = {1,4,5,6}

# my_set_3 = my_set_2.issuperset(my_set_1)

# print(my_set_3)

# my_set = {1,2,3,3,4,4,5}
# # my_tuple = tuple(set([1,2,3,3,4,4,5]))

# for elements in my_set:
#     print(elements)


# import random
# from datetime import datetime
# def execution_time(func):
#     def wrapper(*args, **kwargs):
#         initial_time = datetime.now()
#         func(*args, **kwargs)
#         final_time = datetime.now()
#         time_elapsed = final_time - initial_time
#         print ('Pasaron ' + str(time_elapsed.total_seconds()) + ' segundos')
#     return wrapper

# @execution_time
# def remove_duplicates(some_list):
#     without_duplicates = []
#     for element in some_list:
#         if element not in without_duplicates:
#             without_duplicates.append(element)
#     print('Lista sin duplicados: ', without_duplicates)

# @execution_time
# def remove_set(some_list):
#     without_duplicates = set(some_list)
#     print('Lista sin duplicados: ', without_duplicates)

# def run():
#     random_list = [random.randint(1,10) for _ in range(10000000)]
#     remove_duplicates(random_list)
#     print('\nResultado con sets:')
#     remove_duplicates(random_list)

# if __name__ == '__main__':
#     run()

from datetime import datetime

my_date = datetime.now()

print(my_date)