import random
class Board:
    def __init__(self):
        self.player1 = "X"  # YOUR DEFAULT SIDE
        self.player2 = "O"  # DEFAULT SIDE(BOT)
        self.table = ""
        self.position_list = []
        self.reset_board()
        self.slot = []

    def choose_side(self, side):
        if side.upper() == "X":
            self.player1 = "X"
            self.player2 = "O"
        elif side.upper() == "O":
            self.player1 = "O"
            self.player2 = "X"

    def print_board(self):
        self.table = f"""
                 {self.position_list[0]["position"]} | {self.position_list[1]["position"]} | {self.position_list[2]["position"]} 
                ___|___|___
                 {self.position_list[3]["position"]} | {self.position_list[4]["position"]} | {self.position_list[5]["position"]} 
                ___|___|___
                 {self.position_list[6]["position"]} | {self.position_list[7]["position"]} | {self.position_list[8]["position"]} 
                 """
        print(self.table)

    def reset_board(self):
        self.position_list = []
        self.move_list = []
        for i in range(9):
            self.position_list.append({
                "position": i + 1,
                "status": "empty"
            })

    def mark_position(self, position_num, symbol):
        if position_num < 1 or position_num > 9:
            print("Invalid number! Choose between 1 and 9.")
            return False

        if self.position_list[position_num - 1]["status"] == "empty":
            self.position_list[position_num - 1]["status"] = "marked"
            self.position_list[position_num - 1]["position"] = symbol
            return True
        else:
            return False

    def check_win(self, player):
        win_condition = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        if player == "X":
            current_symbol = self.player1
        else:
            current_symbol = self.player2

        for condition in win_condition:
            if (self.position_list[condition[0]]["position"] == current_symbol and
                    self.position_list[condition[1]]["position"] == current_symbol and
                    self.position_list[condition[2]]["position"] == current_symbol):
                print(f"Congratulations! Player {current_symbol} won the Tic Tac Toe!")
                return True

        return False

    def remain_slot(self):

        self.slot = []
        for remain_slot in self.position_list:
            if remain_slot["status"] == "empty":
                self.slot.append(remain_slot["position"])


new_board = Board()


while True:
    print("1. Choose your side(X or O)")
    print("2. Play a match")
    print("3. Reset the board to start over")
    print("4. Display the current board ")
    print("5. Quit the game")
    option = input("Choose the option: ")

    if option == "1":
        side = input("Choose your side(X or O): ")
        new_board.choose_side(side)

    if option == "2":
        new_board.reset_board()
        new_board.print_board()
        turn = 0
        game_over = False

        while turn < 9 and not game_over:
            #Player 1 (You)
            player_moved = False
            while not player_moved:
                try:
                    number = int(input("Choose the position to mark (1-9): "))
                    if new_board.mark_position(number, symbol=new_board.player1):
                        player_moved = True
                    else:
                        print("That position is already taken! Try another one.")
                except ValueError:
                    print("Please enter a valid integer.")

            print("Your turn:")
            new_board.print_board()
            turn += 1

            #Check Player 1
            if new_board.check_win(new_board.player1):
                game_over = True
                break

            if turn == 9:
                print("Draw!")
                break

            #Player 2 (Bot)
            print("Player 2's turn:")
            new_board.remain_slot()

            bot_choice = random.choice(new_board.slot)
            new_board.mark_position(bot_choice, symbol=new_board.player2)
            new_board.print_board()
            turn += 1

            #Check Player 2
            if new_board.check_win(new_board.player2):
                game_over = True
                break

    if option == "3":
        new_board.reset_board()
        print("Board is clean now")
    if option == "4":
        new_board.print_board()
    if option == "5":
        print("Goodbye!")
        break