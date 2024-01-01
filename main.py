import datetime

def create_board(board_str):
    """ Create the initial board from a string representation. """
    # Split the string into rows and convert each row into a list
    board = [list(row) for row in board_str.split("\n")]
    board = board[1:] # Remove the first row, which is empty
    board = board[:-1] # Remove the last row, which is empty

    return board


def rotate_and_flip_block(block):
    """ Rotate and flip the block to get all unique orientations. """
    # Function to rotate a block
    def rotate(b):
        return [list(row) for row in zip(*b[::-1])]

    # Original and vertically flipped block
    blocks = [block, block[::-1]]

    # Generate rotations for both blocks
    rotations = set()
    for b in blocks:
        for _ in range(4):
            b = rotate(b)
            rotations.add(tuple(map(tuple, b)))  # Add as a tuple of tuples

    # Convert back to list of lists and return unique rotations
    return [list(map(list, b)) for b in rotations]


def print_block(block):
    """ Print a block. """
    print("\n".join([ ''.join(line) for line in block]))


def can_place_block(board, block, position):
    """ Check if a block can be placed at the given position on the board. """
    block_height = len(block)
    block_width = len(block[0])
    board_height = len(board)
    board_width = len(board[0])

    x, y = position

    # Check if block goes out of the board's boundaries
    if x + block_width > board_width or y + block_height > board_height:
        return False

    # Check for overlap with existing blocks
    for i in range(block_height):
        for j in range(block_width):
            if block[i][j] == '#' and board[y + i][x + j] != '.':
                return False

    return True


def solve_board(board, blocks, next_block=0, current_char='A'):
    """ Recursive function to solve the board using backtracking. """
    if next_block >= len(blocks):
        return True  # All blocks placed

    # for rotation in rotate_block(blocks[next_block]):
    for rotation in rotate_and_flip_block(blocks[next_block]):
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_block(board, rotation, (x, y)):
                    # Place the block
                    place_block(board, rotation, (x, y), current_char)
                    # print(current_char, end="")

                    # Recurse with the next block
                    if solve_board(board, blocks, next_block + 1, chr(ord(current_char) + 1)):
                        return True

                    # Remove the block if it didn't lead to a solution
                    place_block(board, rotation, (x, y), '.')
                
    # print()

    return False


def place_block(board, block, position, char):
    """ Place or remove a block on the board. """
    block_height = len(block)
    block_width = len(block[0])
    x, y = position

    for i in range(block_height):
        for j in range(block_width):
            if block[i][j] == '#':
                board[y + i][x + j] = char


def print_board_with_colors(board):
    """
    Print text with each character having a different background color.

    :param text: The string to print.
    :param background_colors: A list of background color codes.
    """
    board_str = "\n".join(["".join(row) for row in board])
    background_colors = ['41', '42', '43', '44', '45', '46', '47', '100', '101', '102', '103', '104', '105']

    assigned_background_colors = dict(zip(set(list(board_str.replace("\n", ""))), background_colors))

    for i, char in enumerate(board_str):
        # Cycle through the background colors
        color = assigned_background_colors.get(char, '40')

        # ANSI escape code: \033[ is the escape character, followed by [background code;30m
        # 30 is for black text color to ensure visibility on different backgrounds
        print(f"\033[{color};30m{char}\033[0m", end="")

    print()  # New line at the end



# Sample initial board configuration
initial_board_str = """
########...
######.....
#######....
#######....
########...
"""


blocks = [
    [
        ["#", " "],
        ["#", "#"],
        [" ", "#"],
        [" ", "#"],
    ],
    [
        ["#", " "],
        ["#", " "],
        ["#", "#"],
        ["#", " "],
    ],
    [
        ["#", "#"],
        ["#", " "],
        ["#", " "],
    ],
    [
        ["#", " "],
        ["#", " "],
        ["#", " "],
        ["#", "#"],
    ],
]



if __name__ == "__main__":
    start_time = datetime.datetime.now()
    initial_board = create_board(initial_board_str)

    print("Initial board:\n")
    for row in initial_board:
        print("".join(row))

    print("\n\n")

    print("Blocks:\n")
    for block in blocks:
        print_block(block)
        print("\n")

    print("\n\n")

    # Reset the initial board and solve it with the given blocks
    solution_found = solve_board(initial_board, blocks)

    # Display the solved board if a solution was found
    if solution_found:
        # import pdb; pdb.set_trace()
        print_board_with_colors(initial_board)
    else:
        print("No solution found.")
    
    end_time = datetime.datetime.now()

    print("\n\nTime taken: %.2f seconds" % (end_time - start_time).total_seconds())
    print("Start time:", start_time.strftime("%H:%M:%S"))
    print("End time:", end_time.strftime("%H:%M:%S"))


# ######## ######## ######## ######## ######## ######## ######## ########
#
#           ALL BLOCKS
#
# ######## ######## ######## ######## ######## ######## ######## ########

# [
#     ["#", "#"],
#     ["#", "#"],
#     ["#", " "],
# ],
# [
#     ["#", " "],
#     ["#", "#"],
# ],
# [
#     ["#", " "],
#     ["#", "#"],
#     ["#", " "],
# ],
# [
#     ["#", " ", " "],
#     ["#", "#", " "],
#     [" ", "#", "#"],
# ],
# [
#     ["#", "#"],
#     ["#", " "],
#     ["#", "#"],
# ],
# [
#     ["#", "#", "#"],
#     ["#", " ", " "],
#     ["#", " ", " "],
# ],
# [
#     ["#", "#", " "],
#     [" ", "#", "#"],
#     [" ", "#", " "],
# ],
# [
#     ["#", " "],
#     ["#", "#"],
#     [" ", "#"],
#     [" ", "#"],
# ],
# [
#     ["#", " "],
#     ["#", " "],
#     ["#", "#"],
#     ["#", " "],
# ],
# [
#     ["#", "#"],
#     ["#", " "],
#     ["#", " "],
# ],
# [
#     ["#", " "],
#     ["#", " "],
#     ["#", " "],
#     ["#", "#"],
# ],
# [
#     ["#", " "],
#     ["#", "#"],
#     [" ", "#"],

# ],
