"""
FIT1045: Sem 1 2023 Assignment 1 (Solution Copy)
"""
import random
import os

def clear_screen():
	"""
	Clears the terminal for Windows and Linux/MacOS.

	:return: None
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
	"""
	Prints the rules of the game.

	:return: None
	"""
	print("================= Rules =================")
	print("Connect 4 is a two-player game where the")
	print("objective is to get four of your pieces")
	print("in a row either horizontally, vertically")
	print("or diagonally. The game is played on a")
	print("6x7 grid. The first player to get four")
	print("pieces in a row wins the game. If the")
	print("grid is filled and no player has won,")
	print("the game is a draw.")
	print("=========================================")


def validate_input(prompt, valid_inputs):
	"""
	Repeatedly ask user for input until they enter an input
	within a set valid of options.

	:param prompt: The prompt to display to the user, string.
	:param valid_inputs: The range of values to accept, list
	:return: The user's input, string.
	"""
	# Implement your solution below
	while True:
		UserInput = input(prompt)
		if UserInput in valid_inputs:
			return UserInput
		else: 
			print("Invalid input, please try again.")


def create_board():
	"""
	Returns a 2D list of 6 rows and 7 columns to represent
	the game board. Default cell value is 0.

	:return: A 2D list of 6x7 dimensions.
	"""
	# Implement your solution below
	row = 6
	column = 7
	board=[]

	#Create columns by adding/appending [0,0,0,0,0,0,0] inside board[]  --> Repeats X6 for rows
	while row > 0:
		createColumns = [0] * column     
		board.append(createColumns)	
		row = row - 1
	else:
		return(board)


def print_board(board):
	"""
	Prints the game board to the console.

	:param board: The game board, 2D list of 6x7 dimensions.
	:return: None
	"""
	# Implement your solution below
	print("========== Connect4 =========")
	print("Player 1: X       Player 2: O\n")
	print("  1   2   3   4   5   6   7")
	print(" ---" * 7)
	for row in board:  						# For the outer [] in board[[1],[2],[3]...] --> [[|],[|],[|]...] Creates first '|' for every row 
		print("|", end="")
		for cell in row:					# For innner [] in board[[1,2,3],[1,2,3]...]
			if cell == 0:
				print("   ", end="|")		# For innner [] in board[[0,0,0]...] --> [[" "," "," "]...]
			elif cell == 1:
				print(" X ", end="|") 		# For innner [] in board[[0,1,0]...] --> [[" "," X "," "]...]
			elif cell == 2:
				print(" O ", end="|") 		# For innner [] in board[[0,0,2]...] --> [[" "," "," O "]...]
		print()
		print(" ---" * 7 )
	print("=============================")
	return("")


def drop_piece(board, player, column):
	"""
	Drops a piece into the game board in the given column.
	Please note that this function expects the column index
	to start at 1.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player who is dropping the piece, int.
	:param column: The index of column to drop the piece into, int.
	:return: True if piece was successfully dropped, False if not.
	"""
	# Implement your solution below
	for row in range(5, -1, -1):#reverse iteration, check from bottom
		if board[row][column - 1] == 0:      
		# try to find the column you want to drop
		#     and iterate from bottom row to top
		#     check whether there is a token      
			board[row][column - 1] = player
			return True
	return False


def execute_player_turn(player, board):
	"""
	Prompts user for a legal move given the current game board
	and executes the move.

	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	valid_inputs = ["1", "2", "3", "4", "5", "6", "7"]
	prompt = f"Player {player}, please select a column (1-7): "

	while True:
		chosen_column = int(validate_input(prompt, valid_inputs))
		successful_drop = drop_piece(board, player, chosen_column)

		if successful_drop:
			break
		else:
			print("That column is full, please try again.")

	return chosen_column


def end_of_game(board):
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""
	# Implement your solution below
	rowBoard = 6
	columnBoard = 7 

	# horizontal win
	for player in [1,2]:
		for row in range(rowBoard):
			for col in range(columnBoard -3):
				if board[row][col] == player & board[row][col+1] == player & board[row][col+2] == player & board[row][col+3] == player:
					return(player)

	# vertical win
	for player in [1,2]:
		for row in range(rowBoard - 3):
			for col in range(columnBoard):
				if board[row][col] == player & board[row+1][col] == player & board[row+2][col] == player & board[row+3][col] == player:
					return (player)

		#   positive diagonal 
	for player in [1,2]:
		for row in range(rowBoard -3):
			for col in range(columnBoard -3):
				if board[row][col] == player & board[row+1][col+1] == player & board[row+2][col+2] == player & board[row+3][col+3] == player:
					return (player)

	# Negative diagonal
	for player in [1,2]:
		for row in range(3, rowBoard):
			for col in range(columnBoard - 3):
				if(board[row][col] == player & board[row-1][col+1] == player & board[row-2][col+2] == player & board[row-3][col+3] == player):
					return(player)

	# Game not over and there are still space on the board                  
	for row in board:
		for col in row:
			if col == 0:
				return (0)

	# Draw & game over if no more space on the board
	counter = 42
	test = 0
	# for player in [1,2]:
	for row in board:
		for col in row:
			if(col == 1 or col ==2):
				counter -= 1
				if counter <= 0:
					return (3)


def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Implement your solution below
	player = 1
	player2 = 2
	result = end_of_game(board)
	# move = execute_player_turn(player, board) 

	while end_of_game(board) == 0:
		move = execute_player_turn(player, board)
		print(print_board(board))
		print("Player 1 dropped a piece into column", move)
		if end_of_game(board) == 1:
			print("player 1 won")
			break 
		move = execute_player_turn(player2, board)
		print(print_board(board))
		print("Player 2 dropped a piece into column", move)
		if end_of_game(board) == 2:
			print("player2 won")
			break


def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	# Implement your solution below
	print("=============== Main Menu ===============")
	print("Welcome to Connect 4!")
	print("1. View Rules")
	print("2. Play a local 2 player game")
	print("3. Play a game against the computer")
	print("4. Exit")
	option = int(input())
	if option == 1:
		print_rules()
	elif option == 2:
		local_2_player_game()
	elif option == 3:
		game_against_cpu()        
	elif option == 4:
		clear_screen()
	else:
		print("Invalid input. Please try again.")
		return main()


def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
	while True:
		column = random.randint(1, 7)
		if drop_piece(board, player, column):
			return column  # Return 1-based column index

# Helper function to simulate a move
def simulate_move(board, player, column):
    temp_board = [row.copy() for row in board]
    if drop_piece(temp_board, player, column):
        return temp_board
    else:
        return None        

def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty. 
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
    # Helper function to simulate a move
	def simulate_move(board, player, column):
		temp_board = [row.copy() for row in board]
		if drop_piece(temp_board, player, column):
			return temp_board
		else:
			return None

	# Check for an immediate win
	for col in range(0, 7):
		temp_board = simulate_move(board, player, col)
		if temp_board and end_of_game(temp_board) == player:
			drop_piece(board, player, col)
			return col 

	# Check for an immediate win for the opponent and block it
	opponent = 3 - player
	for col in range(0, 7):
		temp_board = simulate_move(board, opponent, col)
		if temp_board and end_of_game(temp_board) == opponent:
			drop_piece(board, player, col)
			return col 

	# Play a random move
	while True:
		col = random.randint(0, 7)
		if drop_piece(board, player, col):
			return col 


def cpu_player_hard(board, player):
	"""
	Executes a move for the CPU on hard difficulty.
	This function creates a copy of the board to simulate moves.
	<Insert player strategy here>

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	# Implement your solution below
# Helper function to simulate a move
	def simulate_move(board, player, column):
		temp_board = [row.copy() for row in board]
		if drop_piece(temp_board, player, column):
			return temp_board
		else:
			return None        

    # Defines a function that takes a board and a player as arguments, and analyzes the board's score
	def analyze_board(board, player):
		score = 0
		for col in range(0, 7): #iterates through all columns of the board 
			temp_board = simulate_move(board, player, col) #simulates a move by teh player on the current column 
			if temp_board: 
				count = 0
				for c in range(0, 7): #iterates through all cols of the temp board resulting from the move
					if simulate_move(temp_board, player, c) and end_of_game(simulate_move(temp_board, player, c)) == player:
						count += 1 # If a move in the current col of temp board results in a win for the player, increment the count
                    # Add the count to the score for the current column
				score += count
		return score

    # Calculates the opponent's player number
	opponent = 3 - player
	# Initializes the best column and best score to a default value
	best_col = -1
	best_score = float('-inf')

    # Iterates through a pre-defined list of columns in a specific order, which favors the center columns
	for col in [3, 2, 4, 1, 5, 0, 6]: 
		temp_board = simulate_move(board, player, col)  # Simulates a move by the player on the current column
		if temp_board: # if the move is valid and doesn't result in game over, calc player's score and the opponent's score on temp board
			player_score = analyze_board(temp_board, player)
			opponent_score = analyze_board(temp_board, opponent) # Calculate the difference between the player's score and the opponent's score

			score_diff = player_score - opponent_score
		    # If the difference is greater > current best score, >= to the current best score and a random value is less than 0.5,
            # update the best column and best score

    
			if score_diff > best_score or (score_diff == best_score and random.random() < 0.5):
				best_score = score_diff
				best_col = col

    # If a best column was found, drop a piece by the player in that column and return its index
	if best_col != -1:
		drop_piece(board, player, best_col)
		return best_col

    # If no best column was found, iterate through all columns of the board and drop a piece by the player in the first column that isn't full
	# If no optimal move is found, then fallback to the first available move
	for col in range(0, 7):    # Check if the top row of the column is empty, indicating that the column isn't full
		if board[0][col] == 0:  # Check if column is not full
			if drop_piece(board, player, col): # If the piece is successfully dropped in the column, return its index
				return col


def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	# Implement your solution below
def cpu_player_hard(board, player):    
    def analyze_board(board, player):
        score = 0
        for col in range(0, 7):
            temp_board = simulate_move(board, player, col)
            if temp_board:
                count = 0
                for c in range(0, 7):
                    if simulate_move(temp_board, player, c) and end_of_game(simulate_move(temp_board, player, c)) == player:
                        count += 1
                score += count
        return score

    opponent = 3 - player
    best_col = -1
    best_score = float('-inf')

    for col in [3, 2, 4, 1, 5, 0, 6]:
        temp_board = simulate_move(board, player, col)
        if temp_board:
            player_score = analyze_board(temp_board, player)
            opponent_score = analyze_board(temp_board, opponent)
            score_diff = player_score - opponent_score

            if score_diff > best_score or (score_diff == best_score and random.random() < 0.5):
                best_score = score_diff
                best_col = col

    if best_col != -1:
        drop_piece(board, player, best_col)
        return best_col

    # If no optimal move is found, then fallback to the first available move
    for col in range(0, 7):
        if board[0][col] == 0:  # Check if column is not full
            if drop_piece(board, player, col):
                return col
# Create a new board
board = create_board()

def game_against_cpu():
    # Prompt the user to select difficulty leve
    print("Select difficulty level: ")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    level = int(input())

    # Initialize game board and set starting pl
    board = create_board()
    player = 1

    # Initialize CPU player based on selected d
    if level == 1:
        cpu_player = cpu_player_easy
    elif level == 2:
        cpu_player = cpu_player_medium
    elif level == 3:
        cpu_player = cpu_player_hard
    else:
        print("Invalid input.")
        return

    # Game loop
    while True:
        # Clear console and print game board
        clear_screen()
        print_board(board)

        # Display previous move
        if player == 1:
            print("Last move: CPU player")
        else:
            print("Last move: Player 1")

        # Execute player's turn
        if player == 1:
            execute_player_turn(player, board)
        else:
            cpu_player(board, player)

        # Check if game has ended
        result = end_of_game(board)
        if result != 0:
            clear_screen()
            print_board(board)
            if result == 1:
                print("Player 1 wins!")
            elif result == 2:
                print("CPU player wins!")
            else:
                print("Draw!")
            break

        # Switch to other player
        player = 3 - player


if __name__ == "__main__":
	main()