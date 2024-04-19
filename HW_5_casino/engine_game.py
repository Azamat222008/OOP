import random
from decouple import config
my_money = int(config('my_money'))
class Game:

    def casino_game(self, bet, slot):
        winning_slot = random.randint(1, 10)

        if slot == winning_slot:
            return bet * 2
        else:
            return -bet


    def play_game(self):
        global my_money
        while my_money > 0:
            print(f"Current money: ${my_money}")

            bet = int(input("Place your bet: "))
            slot = int(input("Choose a slot from 1 to 10: "))

            result = self.casino_game(bet, slot)
            my_money += result

            if result > 0:
                print(f"Congratulations! You won ${result}")
            else:
                print(f"Sorry, you lost ${-result}")

            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                break

        print(f"Game over. You finished with ${my_money}")

























