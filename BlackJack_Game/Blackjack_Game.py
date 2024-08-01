import random
from random import randint
def roll():
    return random.randint(1,11)
def player_win():
    print("\t|---------------|")
    print("\t| Выйграл игрок |")
    print("\t|---------------|")
def dealer_win():
    print("\t|---------------|")
    print("\t| Выйграл дилер |")
    print("\t|---------------|")
def game_21_blackjack():
    player_answer = ""
    player_sum, dealer_sum, count_attempt = 0, 0, 0
    player, dealer = True, True
    stop_game = False
    print("\t|-_-_-_-_-_-_-_-_-_-_-_-_-|")
    print("\t|\t\t Игра в 21        |")
    print("\t|_-_-_-_-_-_-_-_-_-_-_-_-_|\n")
    while player_answer != 'нет' and stop_game != True:
        player_answer = input("\tХочешь бросать кубик? (Да/Нет)\n\t").lower()
        if player_answer == 'нет':
            print(f"\n\tСуммарно у игрока {player_sum}, суммарно у дилера {dealer_sum}")
            if count_attempt == 0:
                dealer_win()
            elif dealer_sum > 21:
                player_win()
            elif player_sum == 21:
                player_win()
            elif player_sum > 21:
                dealer_win()
            elif dealer_sum > 21:
                player_win()
            elif dealer_sum > player_sum:
                dealer_win()
            elif dealer_sum == player_sum:
                print("\tНичья\n")
            else:
                player_win()
            break
        player_try = roll()
        player_sum += player_try
        print(f"\tУ игрока выпало {player_try},суммарно у игрока {player_sum} ")
        if count_attempt > 0:
            print(f"\tСуммарно у дилера {dealer_sum}")
        if player_sum == 21 or dealer_sum > 21:
            player_win()
            break
        if player_sum > 21 or dealer_sum == 21:
            dealer_win()
            break
        while dealer_sum <= 16:
            print("\tДилер бросает кубик\n")
            dealer_try = roll()
            dealer_sum += dealer_try
            print(f"\tУ дилера выпало {dealer_try},суммарно у дилера {dealer_sum}")
            if dealer_sum == 21:
                dealer_win()
                stop_game = True
                break
            if dealer_sum > 21:
                player_win()
                stop_game = True
                break
        count_attempt += 1
def menu_game():
    answer = ""
    while answer != 'нет':
        game_21_blackjack()
        answer = input("\tХотите сыграть ещё в 21? (Да/Нет)\n\t").lower()
    else:
        print("\n\tУдачи, хорошего дня!")
menu_game()