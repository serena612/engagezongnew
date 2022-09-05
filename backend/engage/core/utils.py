import operator
from datetime import date, timedelta
from functools import reduce
from random import choice
from string import ascii_uppercase, digits


def find(element, json):
    return reduce(operator.getitem, element.split('.'), json)


def generate_string(n):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(n))


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)
