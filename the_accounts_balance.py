#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def generate_target_number():
    """
    This function generates a random target number between 101 and 999.
    :return: the target number.
    """
    return random.randint(101, 999)


def generate_balance_numbers():
    list_of_balance_numbers = [random.randint(1,10),
                               random.randint(1,10),
                               25, 50, 75, 100]
    return list_of_balance_numbers


def main():
    generate_target_number()
    list_balance_numbers = generate_balance_numbers()


if __name__=='__main__':
    main()