"""
Create following classes
1. Player class
2. Board class
3. Game class
Board Class:
1. Constructor which takes positions_of_snakes (dictionary where head is key, tail is value),
positions_of_ladders (dictionary where key is start of ladder, value is end of ladder)
2. Method is_snake(position) -> Return True if it is snake box else return False.
3. Method is_ladder(position) -> Return True if it is ladder box else return False.
4. Method climb_ladder(ladder_start_box) -> Return the respective index to jump using
position_of_ladders.
5. Method go_down(snake_position) -> Return the respective index to go down using
positions_of_snakes.

Player Class:
1. Constructor which takes name of player, initialise current position as 1 (as player need to
start from 1)
2. roll_dice() method, which will roll dice, on rolling dice it should return random number
between 1 to 6.

Game Class:
1. Create a method start_game() inside which create 2 player objects (say player_1 and
player_2) and board class.
2. Put a while loop and check whether any of the player reaches the box 100, if not continue
the loop, roll dice for player_1, player_2, player_1, player_2 and so on....(check for snake
and ladders using Board class and perform ups and downs accordingly) Until any one
player reaches the box 100. If reached 100, print the winner declaration. Saying “Player
<Player name> wins the game!”.
3. Note that: If player is in 96th box, and his roll gives 5 then 96+5 = 101 (Invalid) at this time,
you should not declare him as winner! He has to exactly to go to 100th box to become
winner.
Sample I/O:
player_1 = Player(“Hari”)
player_2 = Player(“Ganesh”)
positions_of_snakes = {5: 1, 35 : 3}
positions_of_ladders = {7 : 81, 41 : 53}
board = Board(positions_of_snakes, positions_of_ladders)
while (# Write your conditions) :
....
Write all you logic here
....
PRINT THE WINNER!
If any player reaches 5 (as per above example) he should go back to 1 (using go_down as
is_snake(5) returns True. Similarly, if any player reaches 41 (as per above example) he should go
to 53 as is_ladder(41) returns True and so on.... The game should continue until anyone reaches100. Make sure to handle all possible exceptions and also print logs to understand how the game
is going.
A typical sample log is like below
- Player 1 (Hari) rolled 3 and reaches 3
- Player 2 (Ganesh) rolled 4 and reaches 4
- Player 1 (Hari) rolled 2 and reaches 5
- Player 1 (Hari) Snake found and reaches 1
- Player 2 (Ganesh) rolled 3 and reaches 7
- Player 2 (Ganesh) Ladder found and reaches 81 ..... and so on.
"""


class Board:
    def __init__(self, position_of_snake,position_of_ladder):
        self.position_of_snake = position_of_snake
        self.position_of_ladder = position_of_ladder

    def is_snake(self, position):
        return position in self.position_of_snake.keys()

    def is_ladder(self, position):
        return position in self.position_of_ladder.keys()    

    def climb_ladder(self, ladder_start_box):
        return self.position_of_ladder[ladder_start_box]

    def go_down(self, snake_position):
        return self.position_of_snake[snake_position]


class Player:
    def __init__(self,name):
        self.name = name
        self.current_position = 1


    def roll_dice(self):
        import random
        random.seed()
        return random.randrange(1,7)

class Game:
    def start_game(self):
        p1 = Player("Red")
        p2 = Player("Blue")
        players = (p1,p2)
        positions_of_snakes = {5: 1, 35 : 3}
        positions_of_ladders = {7 : 81, 41 : 53}
        board = Board(positions_of_snakes, positions_of_ladders)
        player_turn =1
        while player_turn > 0 and (p1.current_position != 100) and (p2.current_position != 100):
            self.move_payer( players[player_turn % len(players)],board)
            player_turn +=1
            
  
    def move_payer(self, player,board):
        position = player.roll_dice()
        if player.current_position + position > 100:
            return
        player.current_position += position
        if board.is_snake( player.current_position ):
            player.current_position = board.go_down(player.current_position)
            print(f"{player.name} snake found and reaches {player.current_position}")
    
        elif board.is_ladder( player.current_position ):
            player.current_position = board.climb_ladder(player.current_position)            
            print(f"{player.name} ladder found and reaches {player.current_position}")

        print(f"{player.name} rolled {position} and reaches {player.current_position}")
        if player.current_position == 100:
            print(f"{player.name} is WINNER")

g = Game()
g.start_game()

"""
OUTPUT
------

Blue rolled 1 and reaches 2
Red rolled 3 and reaches 4
Blue ladder found and reaches 81
Blue rolled 5 and reaches 81
Red rolled 4 and reaches 8
Blue rolled 4 and reaches 85
Red rolled 6 and reaches 14
Blue rolled 2 and reaches 87
Red rolled 6 and reaches 20
Blue rolled 5 and reaches 92
Red rolled 5 and reaches 25
Blue rolled 1 and reaches 93
Red rolled 4 and reaches 29
Blue rolled 3 and reaches 96
Red snake found and reaches 3
Red rolled 6 and reaches 3
Red rolled 3 and reaches 6
Red rolled 2 and reaches 8
Blue rolled 4 and reaches 100
Blue is WINNER

OUTPUT 2:
-------

Blue snake found and reaches 1
Blue rolled 4 and reaches 1
Red rolled 5 and reaches 6
Blue rolled 1 and reaches 2
Red rolled 5 and reaches 11
Blue rolled 2 and reaches 4
Red rolled 6 and reaches 17
Blue snake found and reaches 1
Blue rolled 1 and reaches 1
Red rolled 3 and reaches 20
Blue rolled 5 and reaches 6
Red rolled 3 and reaches 23
Blue rolled 4 and reaches 10
Red rolled 5 and reaches 28
Blue rolled 6 and reaches 16
Red rolled 5 and reaches 33
Blue rolled 2 and reaches 18
Red rolled 1 and reaches 34
Blue rolled 5 and reaches 23
Red rolled 6 and reaches 40
Blue rolled 1 and reaches 24
Red rolled 4 and reaches 44
Blue rolled 6 and reaches 30
Red rolled 2 and reaches 46
Blue rolled 1 and reaches 31
Red rolled 3 and reaches 49
Blue rolled 3 and reaches 34
Red rolled 4 and reaches 53
Blue rolled 2 and reaches 36
Red rolled 3 and reaches 56
Blue rolled 6 and reaches 42
Red rolled 4 and reaches 60
Blue rolled 3 and reaches 45
Red rolled 4 and reaches 64
Blue rolled 3 and reaches 48
Red rolled 2 and reaches 66
Blue rolled 4 and reaches 52
Red rolled 5 and reaches 71
Blue rolled 1 and reaches 53
Red rolled 3 and reaches 74
Blue rolled 5 and reaches 58
Red rolled 5 and reaches 79
Blue rolled 1 and reaches 59
Red rolled 6 and reaches 85
Blue rolled 5 and reaches 64
Red rolled 6 and reaches 91
Blue rolled 3 and reaches 67
Red rolled 2 and reaches 93
Blue rolled 4 and reaches 71
Red rolled 2 and reaches 95
Blue rolled 1 and reaches 72
Red rolled 2 and reaches 97
Blue rolled 5 and reaches 77
Blue rolled 5 and reaches 82
Blue rolled 2 and reaches 84
Red rolled 1 and reaches 98
Blue rolled 2 and reaches 86
Blue rolled 4 and reaches 90
Red rolled 1 and reaches 99
Blue rolled 4 and reaches 94
Blue rolled 2 and reaches 96
Blue rolled 3 and reaches 99
Red rolled 1 and reaches 100
Red is WINNER
"""

