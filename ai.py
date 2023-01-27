from player import Player
import random
class AI(Player):
    def __init__(self):
        super().__init__()

    def choose_gesture(self):
        self.chosen_choice = random.choice(self.choice_list)
        print(f"AI has picked {self.chosen_choice}")