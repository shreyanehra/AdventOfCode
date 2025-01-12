import numpy as np
class Solution:
    def __init__(self, filepath):
        self.filepath = filepath

    def process_file(self):
        with open(self.filepath, "r") as input_file:
            # Read lines from the file
            grid = input_file.read().splitlines()
            for index,line in enumerate(grid) : 
                grid[index] = list(line)
            
            return grid

    def antena_types(self, grid):
        dict =  {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in dict:
                    dict[grid[i][j]].append((i,j))
                elif grid[i][j].isalnum():
                    dict[grid[i][j]] = [(i,j)]
        
        return dict
    
    def find_antinodes(self):
        #for every pair (p1, p2) of antenas, calculate deltax = xp2 - xp1 and deltay = yp2-yp1
        # find 2 possible antinodes locations by doing p1 - delta and p2 + delta and check if they in map
        num_antinodes = 0
        grid = self.process_file()
        dict = self.antena_types(self.process_file())
        antinodes = set()
        for index,antena_type in enumerate(dict):
            for antena in range(len(dict[antena_type])-1):
                for second_antena in range(antena+1, len(dict[antena_type])):
                    #first antena : antena :   a ((2,3), (4,14))
                    #second antena : seecond_antena to cover all possible pairs of antenas
                    
                    delta_x = dict[antena_type][second_antena][0] - dict[antena_type][antena][0]
                    delta_y = dict[antena_type][second_antena][1] - dict[antena_type][antena][1]
                    #first possible antinode at :
                    x1 = dict[antena_type][antena][0] - delta_x
                    y1 = dict[antena_type][antena][1] - delta_y
                    if 0<=x1<len(grid[0]) and 0<=y1<len(grid) and (x1,y1) not in antinodes:
                        antinodes.add((x1,y1))
                        num_antinodes+=1
                    #second possible nodes at:
                    x2 =dict[antena_type][second_antena][0] + delta_x
                    y2 = dict[antena_type][second_antena][1] + delta_y

                    if 0<=x2<len(grid[0]) and 0<=y2<len(grid) and (x2,y2) not in antinodes:
                        antinodes.add((x2,y2))
                        num_antinodes+=1
        
        return num_antinodes

if __name__=="__main__":
    filepath = "D:\\ACADS\\AOC\\day8\\input.txt"
    sol = Solution(filepath)
    print(sol.find_antinodes())
