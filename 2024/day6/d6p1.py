class Solution:

    def __init__(self, filepath):
        self.filepath = filepath

    def process_file(self):

        with open(self.filepath, "r") as input_file:
            # Read lines from the file
            grid = input_file.read().splitlines()

        position = None  # Initialize position to avoid errors if "^" is not found

        for row_index, line in enumerate(grid):
            grid[row_index] = list(line)  # Convert each line to a list of characters
            if "^" in grid[row_index]:   # Check if "^" is in the current row
                for col_index, char in enumerate(grid[row_index]):
                    if char == "^":
                        position = (row_index, col_index)
                        break  # Stop searching after finding the first "^"

        return grid, position

    def traverse_fwd(self, map, delta_row, delta_column, direction_begin, direction_end):
        return

    def traverse_the_map(self):
        grid, position = self.process_file()
        row, column = position
        
        while(0 <= row < len(grid) and 0 <= column < len(grid[0])):
            while(row >= 1 and grid[row-1][column] != "#"):
                grid[row][column] = "X" # location covered by guard
                grid[row-1][column] = "^"
                row = row-1

            if row == 0: 
                return grid # in the first row so before exiting guard covers one more position
            if grid[row-1][column] == "#":
                grid[row][column] = ">"

            while(column < len(grid[0]) - 1 and grid[row][column+1] != "#"):
                grid[row][column] = "X" # location covered by guard
                grid[row][column+1] = ">"
                column = column + 1

            if column == len(grid[0]):
                return grid
            if grid[row][column+1] == "#":
                grid[row][column] = "V"

            while(row < len(grid) - 1 and grid[row+1][column] != "#"):
                grid[row][column] = "X" # location covered by guard
                grid[row+1][column] = "V"
                row = row + 1

            if row == len(grid)-1:
                return grid
            if grid[row+1][column] == "#":
                grid[row][column] = "<"

            while(column >= 1 and grid[row][column-1] != "#"):
                grid[row][column] = "X" # location covered by guard
                grid[row][column-1] = "<"
                column = column - 1

            if column == 0:
                return grid
            if grid[row][column-1] == "#":
                grid[row][column] = "^"

        return "error"
    
    def countX(self):
        counter = 0
        grid = self.traverse_the_map()
        for r, row in enumerate(grid):
            for c, pos in enumerate(row):
                if grid[r][c]=="X" :
                    counter+=1
        return counter+1

if __name__=="__main__":
    sol = Solution("D:\\ACADS\\AOC\\2024\\day6\\input.txt")
    print(sol.countX())
    
