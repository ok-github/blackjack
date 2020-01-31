from Deck import *
from Player import *
from Hand import *
from os import system, name as osname
from time import sleep

initial_balance = 1000
bet_amt = 0
dealer_hand = []
name = ''
game_on = True

#d = Deck()
#d.shuffle_deck()
#print(d)

#p.get_stats()

def menu():
    print('')

# define our clear function
def clear():
    # for windows
    if osname == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def current_desk(players_loop = False):
    clear()
    print(f"{hand_p.name}'s hand is: {hand_p.get_hand()} ({str(hand_p.get_best_sum())})")

    if players_loop:
        print(f"{hand_d.name}'s hand is: {hand_d.get_first_card_hand()}")
    else:
        print(f"{hand_d.name}'s hand is: {hand_d.get_hand()} ({str(hand_d.get_best_sum())})")

# The main game process
while True:
    print('Welcome to the Black Jack Game!')
    name = input('Enter Your name please: ')

    # Creating player object
    p = Player(name, initial_balance)
    #Creating Deck object
    d = Deck()
    #Shuffle deck
    d.shuffle_deck()

    hand_p = Hand(name)
    hand_d = Hand('Dealer')

    # New game
    while game_on:

        #Making a bet
        while True:
            try:
                bet_amt = int(input(f'Your balance is "{p.get_balance()}". Please make your bet: '))
            except:
                print('Invalid input. Please try again')
            else:
                if (p.bet(bet_amt)):
                    print('Thanks. Your bet is accepted.')
                    sleep(1)
                    break
                else:
                    continue

        # Increment game count
        p.add_game()

        # Empty player's hand
        hand_p.empty_hand()

        # Empty dealer's hand
        hand_d.empty_hand()

        # Give two cards for each player from the deck
        for i in range(2):
            card = d.get_a_card()
            hand_p.add_to_hand(card)

            card = d.get_a_card()
            hand_d.add_to_hand(card)

        #Show current desk
        current_desk(True)

        # Player's game loop
        game_loop = True
        while game_loop:

            choice = ''
            while not(choice == 'H' or choice == 'S'):
                choice = input(f'{p.name}, please make your next step. (H - Hit a card, S - Stay): ').upper()

            if choice == 'H':
                card = d.get_a_card()
                hand_p.add_to_hand(card)
                current_desk(True)

            #hand_p.print_sum()

            # If busts
            if not(hand_p.is_not_busts()):
                print('Sorry, you loose this time')
                #hand_p.print_sum()
                game_loop = False
                break

            '''
            if hand_p.is_21():
                hand_p.print_sum()
                print(f'Wow, you have got a 21! You won {str(bet_amt)}')
                p.credit(bet_amt * 2)
                p.add_won_game()
                game_loop = False
                break
            '''

            if choice == 'S':
                current_desk()
                break

        # Dealer's game loop
        while game_loop:

            if hand_d.get_best_sum() > hand_p.get_best_sum():
                print(f'Dealer won. Sorry, you loose this time')
                game_loop = False
                break

            if hand_d.get_best_sum() == hand_p.get_best_sum():
                print(f'You have a tie! You won and loose 0')
                p.credit(bet_amt)
                game_loop = False
                break

            print('Dealer hits a card...')
            sleep(2)

            card = d.get_a_card()
            hand_d.add_to_hand(card)
            current_desk()
            #hand_d.print_sum()

            if not(hand_d.is_not_busts()):
                #hand_d.print_sum()
                print(f'Dealer is bust. You won {str(bet_amt)}')
                p.credit(bet_amt * 2)
                p.add_won_game()
                game_loop = False
                break

            '''
            if hand_d.is_21():
                #hand_d.print_sum()
                print(f'Dealer has got a 21! Sorry, you loose this time')
                game_loop = False
                break
            '''


        # Check for empty balance
        if p.is_not_empty_balance():
            continue
        else:
            print('Your balance is 0. This game is over.')
            p.get_stats()
            break

        # Check if user wants to continue playing
        '''
        str = ''
        while not(str.upper() == 'Y' or str.upper() == 'N'):
            str = input('Do you want to continue playing? (Y/N): ')
        if str.upper() == 'Y':
            continue
        else:
            print("Ok, let's finish this game!")
            break
        '''


    # Check if user wants to play again
    strc = ''
    while not(strc.upper() == 'Y' or strc.upper() == 'N'):
        strc = input('Do you want to play again? (Y/N): ')
    if strc.upper() == 'Y':
        continue
    else:
        print('See you again!')
        break
