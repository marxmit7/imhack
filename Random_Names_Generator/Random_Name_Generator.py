from random import choice
import csv


def random_name_generator(first, second, x):
    """
        Generates random names.
        Arguments:
         - list of first names
         - list of last names
         - number of random names
    """
    names = []
    for i in range(x):
        names.append("{0} {1}".format(choice(first), choice(second)))
    return set(names)

file=open("First_Names.txt",'r+')

file.seek(0)

first_names=file.readlines()
last_names = ["Smith", "Jones", "Brighton", "Taylor"]
names = random_name_generator(first_names, last_names, 5)
print('\n'.join(names))
