#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import operator
import itertools


def compare_solutions(player_steps, bot_steps, target):
    """
    Compare the player's steps with the bot's solution.
    :param target: the target number.
    :param player_steps: list of player's operations.
    :param bot_steps: list of bot's operations.
    """
    print("\nComparison between your solution and the bot's one:")
    print("-" * 40)
    print("👤 Your steps:")
    for step in player_steps:
        x, symb, y, result = step
        print(f"-> {x} {symb} {y} = {result}")
    print("\n🤖 Bot's steps:")
    for step in bot_steps:
        x, symb, y, result = step
        print(f"-> {x} {symb} {y} = {result}")
    print("-" * 40)

    # Compare final results
    player_final = player_steps[-1][3] if player_steps else None
    bot_final = bot_steps[-1][3] if bot_steps else None

    print(f"\n🎯 Target: {target}")
    print(f"👤 Your final result: {player_final}")
    print(f"🤖 Bot's final result: {bot_final}")

    if player_final == bot_final:
        print("✅ You matched the bot's result!")
    elif abs(player_final - target) < abs(bot_final - target):
        print("👏 Your result is closer! You Won!")
    else:
        print("🤖 The bot's result is closer to the target.")


def get_user_operation(balance_numbers):
    """
    This function gets the user inputs numbers + operator,
    check if they're correct and return them when that's the case.
    :param balance_numbers: the actual balance numbers.
    :return: x input, y, input, the symbol of the operator and the operator itself.
    """
    operator_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
    }

    while True:
        user_input = input('Please enter your operation (ex: 100 +25): ').strip()
        for symbol in operator_map:
            if symbol in user_input:
                parts = user_input.split(symbol)
                if len(parts) == 2:
                    try:
                        x = int(parts[0].strip())
                        y = int(parts[1].strip())
                        if x in balance_numbers and y in balance_numbers:
                            balance_numbers.remove(x)
                            balance_numbers.remove(y)
                            return x, y, symbol, operator_map[symbol]
                        else:
                            print(f"\nNumbers must be in {balance_numbers}. Please try again.")
                    except ValueError:
                        print("\nPlease enter a valid number!")
                break
        else:
            print("Invalid Operator ! Please use +, -, *, / ")


def display_game_state(balance_numbers, target):
    """
    This function displays the game state with icons.
    :param balance_numbers: the balance numbers.
    :param target: the target number.
    :return: a formated display.
    """
    print("\n" + "-" * 40)
    print(f"🎯 Target number: {target}")
    print(f"🔢 Current numbers: {balance_numbers}")
    print("-" * 40)


def bot_solver(numbers, target):
    """
    This function try to solve the equation of finding
    the target number with balance numbers.
    :param numbers: the list of balance numbers.
    :param target:the target number.
    :return: the best path to solve this.
    """
    operators_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.floordiv
    }

    # float('inf') create a float that represent infinity
    best_diff = float('inf')
    best_path = []

    def recursive_solve(nums, path):
        """
        This recursive function is used to solve the equation with
        combinations from itertools.
        :param nums: the list of balance numbers.
        :param path: a list of combinations.
        """
        nonlocal best_diff, best_path

        if len(nums) == 1:
            difference = abs(nums[0] - target)
            if difference < best_diff:
                best_diff = difference
                best_path = path.copy()
            return

        for x,y in itertools.combinations(nums, 2):
            for symb, func in operators_map.items():
                try:
                    result = func(x,y)
                    if result < 0 or result != int(result):
                        continue
                    new_nums = [n for n in nums if n != x and n != y] + [result]
                    new_path = path + [(x, symb, y, result)]
                    recursive_solve(new_nums, new_path)
                except ZeroDivisionError:
                    continue

    recursive_solve(numbers, [])
    return best_path


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
    return [random.randint(1,10),random.randint(1,10),25, 50, 75, 100]


def calculate_operation(chosen_numbers, operator_func, balance_numbers):
    """
    This function calculates the operation, returns the result
    and add it to the list of balance numbers.
    :param chosen_numbers: the number chosen by the user.
    :param operator_func: the operator chosen by the user.
    :param balance_numbers: the actual list of balance numbers.
    :return: the calculated operation, the updated list of balance numbers.
    """
    x, y = chosen_numbers
    try:
        result = operator_func(x, y)
        if result < 0 or result != int(result):
            print("Invalid result: must be positive integer.")
            return None
        balance_numbers.append(result)
        return result
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None


def result_display(x, y, op_symb, result, target_number):
    """
    This function displays the result
    :param x: the first number.
    :param y: the second number.
    :param op_symb: the operator symbol chosen by the user.
    :param result: the result of the calculation.
    :param target_number: the target number.
    :return: formated strings.
    """
    print('-' * 40)
    print(f"🧮 Result of {x} {op_symb} {y} = {result}")
    print(f"🎯 The target number is {target_number} ")
    print('-' * 40)

def ask_continue():
    """
    This function asks the user if they want to continue.
    If not the program ends.
    :return: boolean.
    """
    while True:
        input_choice = input("Do you want to continue? y/n: ").lower().strip()
        if input_choice == 'n':
            print('You are quitting... See you next time!')
            return False
        elif input_choice == 'y':
            return True


def show_bot_solution(list_of_number, target):
    """
    This function shows the bot's solution.
    :param list_of_number: the list of balance numbers.
    :param target: the target number.
    :return: the solution or the closest one.
    """
    solution = bot_solver(list_of_number, target)
    if solution:
        print(f"\n🎯 The target number is: {target}\n🤖 Bot's suggested solution: ")
        for step in solution:
            x, symb, y, result = step
            print(f"-> {x} {symb} {y} = {result}")
    else:
        print("No solution found by the bot.")


def main():
    """
    This is the main function.
    """
    target = generate_target_number()
    balance_numbers = generate_balance_numbers()
    player_steps = []
    initial_numbers = balance_numbers.copy()
    display_game_state(balance_numbers, target)

    # Player loop
    while ask_continue():

        if len(balance_numbers) < 2:
            print("\nNot enough numbers left to continue. Game over!")
            break

        x, y, symbol, chosen_operator = get_user_operation(balance_numbers)
        result = calculate_operation([x, y], chosen_operator, balance_numbers)

        if result is None:
            continue

        player_steps.append((x, symbol, y, result))
        result_display(x, y, symbol, result, target)
        display_game_state(balance_numbers, target)

        if result == target:
            print(f"\n🎉 Congratulations! You reached the target number {target}!")
            break

    # Solution
    if input("\n💡 Would you like to see the solution?  (y/n): ").lower().strip() == 'y':
        bot_steps = bot_solver(initial_numbers, target)
        compare_solutions(player_steps, bot_steps, target)

    print("\n👋 Thanks for playing! Goodbye!")


if __name__=='__main__':
    main()