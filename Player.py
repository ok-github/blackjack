class Player:
    name = ''
    balance = 0
    games_total = 0
    games_won = 0
    player_hand = []

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def bet(self, amount):
        '''
        Make a bet from balance if Player has enought money
        '''
        if amount <= self.balance:
            self.balance -= amount
            return True
        elif amount == 0:
            print('A bet must be greater than 0')
            return False
        else:
            print("You don't have enought money for this bet")
            return False

    def credit(self, amount):
        '''
        Add money to the balance in case when player won the game
        '''
        self.balance += amount

    '''
    def empty_hand(self):
        self.player_hand = []

    def add_to_hand(self, card):
        self.player_hand.append(card)

    def show_hand(self):
        print('Your hand is: ' + ' '.join(self.player_hand))
    '''

    def get_stats(self):
        print(self)

    def get_balance(self):
        return self.balance

    def is_not_empty_balance(self):
        return self.balance > 0

    def add_game(self):
        self.games_total += 1

    def add_won_game(self):
        self.games_won += 1

    def __str__(self):
        return f'Player: "{self.name}"\n' + f'Balance: {self.balance}\n' + f'Games participated: {self.games_total}\n' + f'Games won: {self.games_won}'
