
""" 
Snakes and Ladders Game
This script implements the classic board game "Snakes and Ladders". 
It includes functionality for player movement, dice rolling, handling of snakes and ladders, 
and determining the winning condition.
"""
import sys

class SnakesAndLadders:
    """
    Class to represent the Snakes and Ladders game.
    It manages the game board, players, snakes, ladders, and game mechanics like moving players and checking for win conditions.
    """
    def __init__(self, board_size=100, snakes=None, ladders=None):
        """
        Initializes a new game of Snakes and Ladders.
        :param board_size: Size of the game board, defaults to 100.
        :param snakes: Dictionary mapping snakes' start to end positions.
        :param ladders: Dictionary mapping ladders' start to end positions.
        """
        self.board_size = board_size
        self.player_positions = {}
        self.snakes = snakes if snakes else {16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53, 89: 68, 92: 88, 95: 75, 99: 80}
        self.ladders = ladders if ladders else {2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 78: 98, 87: 94}

    def add_player(self, player_name, token_color):
        self.player_positions[player_name] = {'position': 1, 'color': token_color}

    def roll_dice(self):
        """
        Simulates rolling a dice by generating a random number between 1 and 6.
        :return: A random integer between 1 and 6.
        """
        import random
        return random.randint(1, 6)  # Returns a random number between 1 and 6, simulating a dice roll

    def move_player(self, player_name, roll):
        """
        Moves the player based on the dice roll. Adjusts position for snakes and ladders.
        :param player_name: Name of the player.
        :param roll: Dice roll result.
        """
        if player_name in self.player_positions:
            original_position = self.player_positions[player_name]['position']
            new_position = original_position + roll

            # Player should not move if the roll would take them beyond the board size
            if new_position > self.board_size:
                print(f"{player_name} rolled a {roll}, but needs exactly {self.board_size - original_position} to win. Staying in the same position: {original_position}.")
                return

            # Check for ladders or snakes but not both in a single move
            if new_position in self.ladders:
                new_position = self.ladders[new_position]
                print(f"{player_name} rolled a {roll} and moved from {original_position} to {original_position+roll} where climbed a ladder to {new_position}!")
            elif new_position in self.snakes:
                new_position = self.snakes[new_position]
                print(f"{player_name} rolled a {roll} and moved from {original_position} to {original_position+roll} where was bitten by a snake and fell to {new_position}!")
            else:
                print(f"{player_name} rolled a {roll} and moved from {original_position} to {new_position}.")


            self.player_positions[player_name]['position'] = new_position
        else:
            print(f"Player {player_name} does not exist.")

    def get_player_position(self, player_name):
        return self.player_positions.get(player_name, {}).get('position')

    def check_win(self, player_name):
        return self.get_player_position(player_name) == self.board_size


class SnakesAndLaddersConsole:
    def __init__(self):
        self.game = SnakesAndLadders()
        self.players_added = False

    def start_game(self):
        print("Welcome to Snakes and Ladders!")
        while not self.players_added and len(self.game.player_positions) < 8:
            self.add_players()

        print("\nStarting the game...\n")
        self.play_game()

    def add_players(self):
        
        colors = ["red", "blue", "green", "yellow", "black", "white", "orange", "purple"]
        try:
            num_players = int(input("Enter the number of players (2 to 8): "))
            if num_players < 2 or num_players > 8:
                print("Please enter a number between 2 and 8.")
                return

            for i in range(num_players):
                player_name = input(f"Enter name for player {i+1}: ")
                token_color = colors[i]
                self.game.add_player(player_name, token_color)

            self.players_added = True
        except ValueError:
            print("Invalid input. Please enter a number.")

    
    def play_game(self):
        while True:
            game_over = False
            for player in self.game.player_positions.keys():
                input(f"{player}'s turn. Press 'Enter' to roll the dice.")
                prev_pos = self.game.get_player_position(player)
                roll = self.game.roll_dice()
                self.game.move_player(player, roll)
                position = self.game.get_player_position(player)
                #print(f"{player} rolled a {roll} and moved from {prev_pos} to position {position}.")

                if self.game.check_win(player):
                    print(f"Congratulations {player}, you have won the game!")
                    game_over = True
                    break
            if game_over:
                break
    
# Running the console-based game

if __name__ == "__main__":
    while True:
        choice = input("Do you want to play a new game or exit? (Enter 'play' or 'exit'): ").strip().lower()
        if choice == 'play':
            game_console = SnakesAndLaddersConsole()
            game_console.start_game()
        elif choice == 'exit':
            print("Exiting the game. Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 'play' or 'exit'.")

