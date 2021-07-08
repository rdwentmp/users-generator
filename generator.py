import csv
import random
import string

users = [i for i in range(0, 10)]
last_names = ["User%d" % user for user in users]


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


def first_names():
    return ["test" + get_random_string(20)]


def email_addresses():
    return ["test" + get_random_string(20) + "@myemail.com"]


i = 1
while i <= 1000:
    with open('users.csv', 'a') as csv_out:
        writer = csv.writer(csv_out)
        writer.writerows(zip(first_names(), email_addresses()))
        i += 1