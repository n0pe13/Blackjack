

# Building the game "Blackjack" using OOP
# Face cards = 10, Ace = 11

import random
import itertools
import sys

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.card_val = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 10, 10, 10]
        self.card_deck = list(itertools.chain.from_iterable(itertools.repeat(x, 4) for x in self.card_val)) # Repeat card_val values up to 52


    # Shuffle and build deck
    def build_deck(self):

        for shuff in range(len(self.card_deck)):
            s = random.randint(0, shuff)
            self.card_deck[shuff], self.card_deck[s] = self.card_deck[s], self.card_deck[shuff]

        return self.card_deck

    # Remove cards once they have been played
    def remove_cards(self, rm_card: int):
        
        try:
            self.card_deck.remove(rm_card)
            return self.card_deck
        except ValueError:
            super().build_deck()
            return self.card_deck.remove(rm_card)
        

class Game(Deck):
    user_wallet = 100
    pot = 0

    def __init__(self):
        self.user_card_count = 0
        self.computer_card_count = 0
        self.break_value = 21
        super().__init__()

    @classmethod
    def set_bet(cls):

        b = True
        bet = int(input("[+] How much would you like to bet? "))

        while b:
            if cls.user_wallet >= bet:
                cls.user_wallet -= bet
                cls.pot = cls.pot + bet * 2
                print(f"\nPot --> ${cls.pot}")
                b = False
                return cls.pot, cls.user_wallet
            elif cls.user_wallet < bet:
                print("[-] Not enough funds available in your wallet")
                bet = int(input("[+] How much would you like to bet? "))
            else:
                print("[-] You are completely broke. Goodbye")
                sys.exit(0)

    def computer_get_hand(self):
    
        computer_hand = random.choices(super().build_deck(), k=2)
        
        for pc in computer_hand:
            self.computer_card_count += pc
            super().remove_cards(pc)
            if self.computer_card_count <= 10:
                next_hand = random.choice(super().build_deck())
                self.computer_card_count += next_hand
                super().remove_cards(next_hand)
      
        return self.computer_card_count
    
    def user_get_hand(self):
        
        user_hand = random.choice(super().build_deck())

        self.user_card_count += user_hand
        super().remove_cards(user_hand)

        return self.user_card_count

    @classmethod
    def show_pot(cls):

        return cls.pot
    
    @classmethod
    def show_wallet(cls):

        return cls.user_wallet

    @classmethod
    def win(cls):

        print("[W] You win!")
        cls.user_wallet += cls.pot
        cls.pot = 0
        print(f"\nWallet --> ${cls.show_wallet()}\n")

        return cls.pot, cls.user_wallet

    @classmethod
    def lose(cls):

        print("[L] You lose!")
        cls.pot = 0
        print(f"\nWallet --> ${cls.show_wallet()}\n")

        return cls.pot, cls.user_wallet
    
    @classmethod
    def tie(cls):

        print("[T] Tie!")
        cls.user_wallet += int(cls.pot / 2)
        cls.pot = 0
        print(f"\nWallet --> ${cls.show_wallet()}\n")

        return cls.pot, cls.user_wallet

    def play_again(self):
     
        play = input("[+] Play Again ('y' or 'n')? ")
        if play == 'y':
            self.user_card_count = 0
            self.computer_card_count = 0
            super().build_deck()
            self.set_bet()
        else:
            sys.exit(0)
        
        return play


    def start_game(self):

        start = True
        self.set_bet()
        while start:
            hit_stay = input("\n[+] Hit or Stay ('h' or 's')?: ")
            if hit_stay == 'h':
                print(f"[!] Your hand total is {self.user_get_hand()}")
                if self.user_card_count > self.break_value:
                    self.lose()
                    self.play_again()
                    start = True
            elif hit_stay == 's':
                print(f"[!] The computers hand total is {self.computer_get_hand()}")
                start = False
                if self.computer_card_count > self.break_value and self.user_card_count <= self.break_value:
                    self.win()
                    self.play_again()
                    start = True
                elif self.computer_card_count == self.user_card_count:
                    self.tie()
                    self.play_again()
                    start = True
                elif self.computer_card_count <= self.break_value and self.computer_card_count > self.user_card_count:
                    self.lose()
                    self.play_again()
                    start = True
                elif self.computer_card_count < self.user_card_count and self.computer_card_count < self.break_value and self.user_card_count < self.break_value:
                    self.win()
                    self.play_again()
                    start = True
                else:
                    self.win()
                    self.play_again()
                    start = True
def main():

    print("\n~Welcome to Blackjack~\n")

    g = Game()
    
    print(f"Pot --> ${g.show_pot()}")
    print(f"Wallet --> ${g.show_wallet()}\n")

    g.start_game()
    
    
if __name__ == '__main__':
    main()



  
    
    
      

    
    

    #c = Card(3, "Hearts")
    #print(c.value)