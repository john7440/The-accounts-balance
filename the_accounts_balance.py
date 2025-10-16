#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import operator

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


def user_number_choice(list_of_balance_numbers):
    while True:
        try:
            user_input = input(f"Which number would you like to balance? choose 2 in {list_of_balance_numbers} ").split()
            chosen_numbers = [int(num) for num in user_input]
            if len(chosen_numbers) == 2 and all(num in list_of_balance_numbers for num in chosen_numbers):
                for num in chosen_numbers:
                    list_of_balance_numbers.remove(num)
                return chosen_numbers, list_of_balance_numbers
            else:
                print(f"Invalid choice. Please choose 2 numbers from {list_of_balance_numbers}.")
        except ValueError:
            print("Please enter valid integers separated by space.")


def choose_operator():
    operator_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    while True:
        user_choice = input('Please choose the operator (+, -, *, /): ')
        if user_choice in operator_map:
            return user_choice, operator_map[user_choice]
        else:
            print("Please enter a valid operator.")

def calculate_operation(chosen_numbers, cal_operator):
    x, y = chosen_numbers
    return cal_operator(x, y)


def result_display(chosen_numbers, op_symb, result):
    print(f"Result of {chosen_numbers[0]} {op_symb} {chosen_numbers[1]} = {result}")

def main():
    generate_target_number()
    list_balance_numbers = generate_balance_numbers()
    chosen_numbers, new_list_of_balance_number = user_number_choice(list_balance_numbers)
    symbol, chosen_operator = choose_operator()
    result = calculate_operation(chosen_numbers, chosen_operator)
    result_display(chosen_numbers, symbol, result)



if __name__=='__main__':
    main()