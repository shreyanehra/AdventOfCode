import re

class Solution:
    def __init__(self, filepath):
        self.filepath = filepath
        self.num_XMAS = 0
        self.matrix = []

    def process_file(self):
        """
        Convert the contents of the file into a 2D matrix.
        """
        with open(self.filepath, 'r') as input_file:
            self.matrix = [list(line.strip()) for line in input_file if line.strip()]

    def find_and_add(self, char_str):
        """
        Find and count instances of "XMAS" and "SAMX" in the given string.
        """
        pattern1 = r"XMAS"
        pattern2 = r"SAMX"
        group_xmas = re.findall(pattern1, char_str)
        group_samx = re.findall(pattern2, char_str)
        self.num_XMAS += len(group_xmas) + len(group_samx)

    def xmas_instances(self):
        """
        Look for "XMAS" and "SAMX" in rows, columns, and diagonals.
        """
        self.process_file()
        
        if not self.matrix:
            return 0
        
        row_len = len(self.matrix)
        col_len = len(self.matrix[0])

        # Check rows
        for row in self.matrix:
            row_str = ''.join(row)
            self.find_and_add(row_str)

        # Check columns
        for col in zip(*self.matrix):
            col_str = ''.join(col)
            self.find_and_add(col_str)

        # Check diagonals (top-left to bottom-right)
        for d in range(row_len + col_len - 1):
            diagonal = []
            for i in range(row_len):
                j = d - i
                if 0 <= j < col_len:
                    diagonal.append(self.matrix[i][j])
            if diagonal:
                self.find_and_add(''.join(diagonal))

        # Check anti-diagonals (top-right to bottom-left)
        for d in range(row_len + col_len - 1):
            anti_diagonal = []
            for i in range(row_len):
                j = d - i + col_len -1
                if 0 <= j < col_len:
                    anti_diagonal.append(self.matrix[i][j])
            if anti_diagonal:
                self.find_and_add(''.join(anti_diagonal))

        return self.num_XMAS

    def x_shaped_mas(self):
        self.process_file()
        
        if not self.matrix:
            return 0
        
        row_len = len(self.matrix)
        col_len = len(self.matrix[0])
        x_MAS_count = 0
        for row in range(1,row_len-1):
            for col in range(1, col_len-1):
                if self.matrix[row][col]=='A':
                    if (self.matrix[row-1][col-1]=='S' and self.matrix[row+1][col+1]=='M') or (self.matrix[row-1][col-1]=='M' and self.matrix[row+1][col+1]=='S'):
                        if(self.matrix[row-1][col+1]=='S' and self.matrix[row+1][col-1]=='M') or (self.matrix[row-1][col+1]=='M' and self.matrix[row+1][col-1]=='S'):
                            x_MAS_count+=1
        
        return x_MAS_count

if __name__ == "__main__":
    filepath = "D:\\ACADS\\AOC\\2024\\day4\\input4.txt"  # Ensure correct file extension
    sol = Solution(filepath)
    print(sol.x_shaped_mas())
