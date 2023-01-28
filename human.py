from player import Player
class Human(Player):
    def __init__(self):
        super().__init__()
        
    def choose_gesture(self):
        self.chosen_choice = input(f"Please make your choice from this list: {self.choice_list}.")
        if self.chosen_choice == 'Rock':
            print("Human has picked rock")
        elif self.chosen_choice == 'Paper':
            print("Human has picked paper")
        elif self.chosen_choice == 'Scissor':
            print("Human has picked scissor")
        elif self.chosen_choice == 'Lizard':
            print("Human has picked lizard")
        elif self.chosen_choice == 'Spock':
            print("Human has picked spock")
        else:
            print("Invalid input. Enter your choice from the list.")
            self.chosen_choice = input(f"Please make your choice from this list: {self.choice_list}.")

    def action(self, rival):
        
