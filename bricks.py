# def read_input(args):


# Reading input:
m, n = map(int, input().split())  # M - rows, N - columns

# empty list soon to be matrix
row_one = []

# reading the rows of the matrix from the input
while True:
    raw_line = input()
    if not raw_line:
        break
    row_one.append(raw_line.split())


# Validating the input:
valid_input = True
comment = ''

#   - less than 100:
if (1 < m < 100) and (1 < n < 100):
    if (m % 2 != 0) or (n % 2 != 0):
        valid_input = False
        comment += 'M and N should be even numbers.\n'
else:
    valid_input = False
    comment += 'M and N should not exceed 100.\n'

#   - exact numbers of row/columns:
if len(row_one) != m:
    valid_input = False
    comment += f'Number of rows is not {m}\n'
for line in row_one:
    if len(line) != n:
        valid_input = False
        comment += f'Number of columns is not {n}\n'
        break

#   - brick over 3 boxes:
available_nums = [a for n in row_one for a in n]
available_nums = sorted(available_nums)[::-1]

if len(available_nums) % 2 != 0:
    valid_input = False
    comment += f'Each brick should be rectangular of size 1 × 2\n'
else:
    pairs = []
    for i in range(len(available_nums)):
        pairs += available_nums[i]
        if len(pairs) > 1:
            if pairs[-1] == pairs[-2]:
                pairs.pop()
                pairs.pop()

    if pairs:
        valid_input = False
        comment += f'Each brick should be rectangular of size 1 × 2\n'

if not valid_input:
    print(comment)
    exit(-1)

print("Input:")
[print(j) for j in row_one]
row_two = ([[0 for x in j] for j in row_one])

while available_nums:
    for r in range(m):
        for c in range(n):
            if r == m-1:
                if c == n-1:
                    pass
                elif row_one[r][c] != row_one[r][c + 1]:
                    if row_two[r][c] == 0 and row_two[r][c + 1] == 0:
                        row_two[r][c] = available_nums[-1]
                        row_two[r][c + 1] = available_nums[-2]
                        available_nums.pop()
                        available_nums.pop()

            elif c == n-1:
                if row_one[r][c] != row_one[r + 1][c]:
                    if row_two[r][c] == 0 and row_two[r + 1][c] == 0:
                        row_two[r][c] = available_nums[-1]
                        row_two[r + 1][c] = available_nums[-2]
                        available_nums.pop()
                        available_nums.pop()

            elif row_one[r][c] != row_one[r][c+1]:
                if row_two[r][c] == 0 and row_two[r][c+1] == 0:
                    row_two[r][c] = available_nums[-1]
                    row_two[r][c+1] = available_nums[-2]
                    available_nums.pop()
                    available_nums.pop()

            elif row_one[r][c] != row_one[r+1][c]:
                if row_two[r][c] == 0 and row_two[r+1][c] == 0:
                    row_two[r][c] = available_nums[-1]
                    row_two[r+1][c] = available_nums[-2]
                    available_nums.pop()
                    available_nums.pop()


def print_matrix(num_matrix):
    num_r = len(num_matrix)
    num_c = len(num_matrix[0])
    new_r = num_r * 2 + 1
    new_c = num_c * 2 + 1

    new_matrix = [['*' for i in range(new_c)]]
    new_matrix.append(["*" for j in range(new_r - 1)])


[print(r) for r in row_two]
