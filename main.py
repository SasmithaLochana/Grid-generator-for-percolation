import datetime
import random
import sys

from prettytable import PrettyTable, SINGLE_BORDER

# Get the dimensions of the grid from the command line arguments
if len(sys.argv) > 1:
    try:
        rows, columns = map(int, sys.argv[1].split("x"))
    except ValueError:
        # handle non-integer arguments
        print(
            "Invalid grid dimensions!\nPlease provide two integer values by splitting them using 'x'.\nDo not use any spaces among the values.\nE.g. 3x5.")
        sys.exit(1)
else:
    rows, columns = 5, 5

# ensure dimensions are within the allowed range
if not (3 <= rows <= 9) or not (3 <= columns <= 9):
    print("Invalid grid dimensions! \nPlease provide two integer values between 3 and 9 (inclusive).\nE.g. 3x9")
    sys.exit(1)

# Create a list of empty cell coordinates
empty_cells = [(i, j) for i in range(rows) for j in range(columns)]

# Randomly select a number of empty cells
num_empty_cells = random.randint(0, int(len(empty_cells) * 0.2))
empty_cells = random.sample(empty_cells, num_empty_cells)

# Create the grid using a nested for loop
grid = []
for i in range(columns):
    col = []
    for j in range(rows):
        # If the current cell is an empty cell, add an empty string to the row
        if (i, j) in empty_cells:
            col.append("")
        else:
            # Otherwise, add a random 2-digit number to the row
            col.append(random.randint(10, 99))
    # Add the column to the grid
    grid.append(col)

# Create a list to store the percolation status of each column
percolation_status = []

# Check the percolation status of each column
for col in grid:
    # Add the percolation status for the current column to the list

    if "" in col:
        percolation_status.append("NO")
    else:
        percolation_status.append("OK")

table = PrettyTable()
for col in grid:
    table.add_column("", col)

# create borders around numbers
table.header = False
table.hrules = True
table.vrules = True
table.format = True
table.set_style(SINGLE_BORDER)

# Add the percolation status column to the grid
table.add_row(percolation_status)

# Print the grid
print(table)

# saving the result as html & text files
filename = "20220216_" + str(datetime.datetime.now()).replace(":", ".")

file = open(filename + ".html", "w", encoding="utf-8")
file.write(table.get_html_string())
file.close()

table.border = False
file = open(filename + ".txt", "w", encoding="utf-8")
file.write(table.get_string())
file.close()

print("Wrote to files " + filename + ".html and " + filename + ".txt!")
