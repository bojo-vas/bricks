def validate_input(r, c, matrix):
    """ Validating the input """

    valid_input = True  # boolean to store if the input was valid
    comment = ''    # comment - only used if the input was not valid for clarity

    # valid area of less than 100 lines/columns:
    if (1 < r < 100) and (1 < c < 100):
        if (r % 2 != 0) or (c % 2 != 0):
            valid_input = False
            comment += 'M and N should be even numbers.\n'
    else:
        valid_input = False
        comment += 'M and N should be less than 100.\n'

    # exact numbers of row/columns:
    if len(matrix) != r:
        valid_input = False
        comment += f'Number of rows is not {r}\n'
    for line in matrix:
        if len(line) != c:
            valid_input = False
            comment += f'Number of columns is not {c}\n'
            break

    # check for bricks with different sizes:
    brick_nums = [num for row in matrix for num in row]  # list of all numbers (strings) used for bricks
    brick_nums = sorted(brick_nums)[::-1]

    # if the length of the list is not odd there is no way the input is valid
    # (this condition is not even possible if M and N are even numbers)
    if len(brick_nums) % 2 != 0:
        valid_input = False
        comment += f'Each brick should be rectangular of size 1 × 2\n'
    else:
        for brick in brick_nums:
            count = brick_nums.count(brick)  # appearance of the number (string) in the list should be exactly 2
            if count != 2:
                valid_input = False
                comment += f'Each brick should be rectangular of size 1 × 2\n'
                break

    if not valid_input:
        return valid_input, comment
    return valid_input, brick_nums


def format_matrix(matrix):
    """ Creating new matrix to fit the requirements of sell separation
    and displaying brick numbers up to 4 digits """

    length = len(matrix)  # number of rows
    width = len(matrix[0])  # number of columns
    new_len = length * 2 + 1  # number of rows for the new matrix (for used separators between "bricks")
    new_wid = width * 2 + 1   # number of columns for the new matrix
    asterisk = '*'  # sign used for separating bricks
    dash = '-'  # sign used for separating numbers in same brick

    # creating new matrix with above mentioned rows and columns and populated with asterisk sign -
    # ":4" - for displaying up to 4 digit numbers
    new_matrix = [[f'{asterisk:4}' for _ in range(new_wid)] for _ in range(new_len)]

    for r in range(length):
        for c in range(width):
            new_matrix[2*r+1][2*c+1] = f"{matrix[r][c]:4}"

    for r in range(1, new_len-1, 2):
        for c in range(1, new_wid-1, 2):
            if r < new_len-2:
                if new_matrix[r][c] == new_matrix[r+2][c]:
                    new_matrix[r+1][c] = f'{dash:4}'
            if c < new_wid-2:
                if new_matrix[r][c] == new_matrix[r][c+2]:
                    new_matrix[r][c+1] = f'{dash:4}'

    return new_matrix


def draw_layer(layer_one, available_bricks):
    """ Create and populate new layer of 'bricks' in a way that no brick in it lies exactly
    on a brick from the first layer or return message and exit code "-1" if impossible"""

    # Creating '0' matrix for the new layer
    layer_two = ([[0 for x in j] for j in layer_one])
    all_bricks = len(available_bricks)  # count of all available brick numbers (each pair is counted twice)
    operations_counter = 0  # Number of cycles accomplished to return the new layer

    while available_bricks:
        for r in range(len(layer_one)):
            for c in range(len(layer_one[0])):
                operations_counter += 1
                # usually operations needed are equal to the multiplication of rows and columns (all_bricks),
                # here we take a security coefficient of 2 before breaking the WHILE with "No solution message"
                if operations_counter == 2 * all_bricks:
                    print("No solution exist")
                    exit(-1)
                if r == len(layer_one) - 1:
                    if c == len(layer_one[0]) - 1:
                        pass
                    elif layer_one[r][c] != layer_one[r][c + 1]:
                        if layer_two[r][c] == 0 and layer_two[r][c + 1] == 0:
                            layer_two[r][c] = available_bricks[-1]
                            layer_two[r][c + 1] = available_bricks[-2]
                            available_bricks.pop()
                            available_bricks.pop()

                elif c == len(layer_one[0]) - 1:
                    if layer_one[r][c] != layer_one[r + 1][c]:
                        if layer_two[r][c] == 0 and layer_two[r + 1][c] == 0:
                            layer_two[r][c] = available_bricks[-1]
                            layer_two[r + 1][c] = available_bricks[-2]
                            available_bricks.pop()
                            available_bricks.pop()

                elif layer_one[r][c] != layer_one[r][c + 1]:
                    if layer_two[r][c] == 0 and layer_two[r][c + 1] == 0:
                        layer_two[r][c] = available_bricks[-1]
                        layer_two[r][c + 1] = available_bricks[-2]
                        available_bricks.pop()
                        available_bricks.pop()

                elif layer_one[r][c] != layer_one[r + 1][c]:
                    if layer_two[r][c] == 0 and layer_two[r + 1][c] == 0:
                        layer_two[r][c] = available_bricks[-1]
                        layer_two[r + 1][c] = available_bricks[-2]
                        available_bricks.pop()
                        available_bricks.pop()

    return layer_two


if __name__ == "__main__":
    # Reading input:
    m, n = map(int, input().split())  # M - rows, N - columns

    # empty list soon to be matrix
    first_layer = []

    # reading each row of the matrix from the input (without validation)
    # "Enter" should be pressed again after last row input (being able to check if rows != M)
    while True:
        raw_line = input().split()
        if not raw_line:
            break
        first_layer.append(raw_line)

    # validating the input and returning list of strings (available brick numbers) or error message if not valid
    validation, bricks_or_message = validate_input(m, n, first_layer)

    if not validation:
        print(bricks_or_message)
        exit(-1)

    # populating the new layer (if exist)
    new_layer = draw_layer(first_layer, bricks_or_message)

    # draw brick walls
    result = format_matrix(new_layer)

    # print the solution
    [print(*x) for x in result]
