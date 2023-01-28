from human import Human
from ai import AI

class Game:
    def __init__(self):
        self.human = Human()
        self.ai = AI()
        
    def run_game(self):    
        self.greeting()
        self.number_of_players()
        self.match_phase()
        self.victory_display()
        pass 
 
    def greeting(self):
        print("Welcome to the Game of Chance Tournament of Rock Paper Scissor Lizard Spock")
        
    def number_of_players(self):
        user_input = input("How many players will there be.")
        if user_input = 1:
            self.human.choose_gesture.action(self.ai.choose_gesture)
        pass
    
    def match_phase(self):
        print("Round Start!"")
        number_of_games = 0
        while number_of_games == True:
            if number_of_games == 4:
                number_of_games == False
                print("The games is over!")
            else:
                print("Round Begin!")
                number_of_games += 1
        pass

    def victory_display(self):
        pass