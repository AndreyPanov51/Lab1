white = "\x1b[107m"
reset = "\x1b[0m"
size  = 5

for row in range(2 * size + 1):
    line = ""
    for c in range(3):
        for col in range(4 * size + 1):
            if c!=0 and col==0:
                next
            elif abs(row - size) + abs(col - size) <= size:
                line += white + "  " + reset
            elif abs(row - size) + abs(col - 3 * size ) <= size:
                line += white + "  " + reset
            else:
                line += "  "
    print(line)