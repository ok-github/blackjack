class Hand:
    name = ''
    hand = []
    summ = []

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.summ = [0]

    def empty_hand(self):
        self.hand = []
        self.summ = [0]

    def add_to_hand(self, card):
        self.hand.append(card)
        self.calc_hand()

    def get_hand(self):
        return ' '.join(self.hand)

    def get_first_card_hand(self):
        return self.hand[0] + ' XX'

    def calc_hand(self):
        self.summ = [0]

        def add_all_sums(arr, val):
            for i in range(len(arr)):
                arr[i] += val

        for card in self.hand:
            card = card[1:]
            try:
                add_all_sums(self.summ, int(card))
            except ValueError:
                if card == 'J' or card == 'Q' or card == 'K':
                    add_all_sums(self.summ, 10)
                elif card == 'A':
                    sum_1 = self.summ.copy()
                    sum_11 = self.summ.copy()
                    add_all_sums(sum_1, 1)
                    add_all_sums(sum_11, 11)
                    self.summ = sum_1 + sum_11

    def is_not_busts(self):
        #self.calc_hand()
        for i in self.summ:
            if i <= 21:
                return True
        return False

    def is_21(self):
        #self.calc_hand()
        for i in self.summ:
            if i == 21:
                return True
        return False

    def get_best_sum(self):
        #self.calc_hand()
        if len(self.summ) == 1:
            return self.summ[0]
        else:
            return max([i for i in self.summ if i <= 21], default = min([i for i in self.summ]))

    def print_sum(self):
        #self.calc_hand()
        if len(self.summ) == 1:
            print(f"{self.name}'s Hand sum is: {self.summ[0]}")
        else:
            print(f"{self.name}'s possible Hand sums are:" + ' '.join([str(i) for i in self.summ]))
