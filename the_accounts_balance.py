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
    """
    This function generates 2 random balance numbers between 1 and 10,
    and add it to a list of balance numbers.
    :return: the list of balance numbers.
    """
    list_of_balance_numbers = [random.randint(1,10),
                               random.randint(1,10),
                               25, 50, 75, 100]
    return list_of_balance_numbers


def user_number_choice(list_of_balance_numbers):
    """
    This function asks the user to choose 2 number of balance numbers and
    check if they are valid.
    :param list_of_balance_numbers: the actual list of balance numbers.
    :return: the choice of the user.
    """
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
    """
    This function asks the user to choose an operator and return it.
    :return: an operator.
    """
    operator_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
    }

    while True:
        user_choice = input('Please choose the operator (+, -, *, /): ')
        if user_choice in operator_map:
            return user_choice, operator_map[user_choice]
        else:
            print("Please enter a valid operator.")


def calculate_operation(chosen_numbers, cal_operator, list_of_balance_numbers):
    """
    This function calculates the operation, returns the result
    and add it to the list of balance numbers.
    :param chosen_numbers: the number chosen by the user.
    :param cal_operator: the operator chosen by the user.
    :param list_of_balance_numbers: the actual list of balance numbers.
    :return: the calculated operation, the updated list of balance numbers.
    """
    x, y = chosen_numbers
    result = cal_operator(x, y)
    list_of_balance_numbers.append(result)
    return result, list_of_balance_numbers


def result_display(chosen_numbers, op_symb, result, target_number):
    """
    This function displays the result
    :param chosen_numbers: the number chosen by the user.
    :param op_symb: the operator symbol chosen by the user.
    :param result: the result of the calculation.
    :param target_number: the target number.
    :return: formated strings.
    """
    print(f"\nResult of {chosen_numbers[0]} {op_symb} {chosen_numbers[1]} = {result}")
    print(f"\nThe target number is {target_number} ")


def ask_continue():
    """
    This function asks the user if they want to continue.
    If not the program ends.
    :return: boolean
    """
    while True:
        input_choice = input("Do you want to continue? y/n: ").lower().strip()
        if input_choice == 'y':
            return True
        else:
            print('You ended the programme! See you next time!')
            return False


def main():
    """
    This is the main function.
    """
    target = generate_target_number()
    list_balance_numbers = generate_balance_numbers()
    print(f"\nThe target number is {target}  <======")
    while ask_continue():
        chosen_numbers, new_list_of_balance_number = user_number_choice(list_balance_numbers)
        symbol, chosen_operator = choose_operator()
        result, updated_list_of_numbers = calculate_operation(chosen_numbers, chosen_operator, new_list_of_balance_number)
        result_display(chosen_numbers, symbol, result, target)


if __name__=='__main__':
    main()