white = "\x1b[107m"
reset = "\x1b[0m"
size = 5
num_diamonds = 14
total_width = num_diamonds * (2 * size) + 1
for row in range(2 * size + 1):
    line = ""
    for col in range(total_width):
        local_col = col % (2 * size)
        if abs(row - size) + abs(local_col - size) <= size:
            line += white + " " + reset
        else:
            line += " "
    print(line)