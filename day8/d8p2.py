from d8p1 import Solution
import numpy as np
class Solution2:
    def __init__(self, filepath):
        self.filepath = filepath
        self.sol2 = Solution(self.filepath)

    def define_grid_find_antenas(self):
        self.grid = self.sol2.process_file() #assigns the grid
        self.dict_antenas = self.sol2.antena_types(self.grid)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])

    #f = unique frequency of a particular antena type
    def pos_on_grid(self, f, index_in_dicts_keys_value ):
        self.define_grid_find_antenas()
        # returning corresponding x and y as (x,y) - a tuple
        return (self.dict_antenas[f][index_in_dicts_keys_value][0], self.dict_antenas[f][index_in_dicts_keys_value][1])

    def find_possible_antinode_pos(self, pos1, pos2, factor):
        '''
        pos1 : position of antena 1
        pos2 : position of antena2
        return : 2 tuples possible antenode positions
        '''
        pos1 = np.array(pos1)
        pos2 = np.array(pos2)
        possible_an1 = pos1 - factor * (pos2 - pos1)
        possible_an2 = pos2 + factor*(pos2 - pos1)

        return (possible_an1, possible_an2)

    def is_inside_grid(self, pos):
        self.define_grid_find_antenas()
        if(0<=pos[0]<self.rows and 0<=pos[1]<self.cols):
            return True
        return False

    def find_all_harmonic_antinodes(self):
        antinodes = set() #initialising empty set 
        self.define_grid_find_antenas()
        

        for f in self.dict_antenas:
            for antena1 in range(len(self.dict_antenas[f])-1):
                for antena2 in range(antena1+1,len(self.dict_antenas[f])):
                    
                    pos_a1 = self.pos_on_grid(f, antena1)
                    pos_a2 = self.pos_on_grid(f, antena2)
                    antinodes.add(pos_a1)
                    antinodes.add(pos_a2)
                    factor = 1
                    an1 = self.find_possible_antinode_pos(pos_a1, pos_a2, factor)[0]                 
                    an2 = self.find_possible_antinode_pos(pos_a1, pos_a2, factor)[1]
                    while( self.is_inside_grid(an1) or self.is_inside_grid(an2)):
                        an1 = tuple(an1)
                        an2 = tuple(an2)
                        if self.is_inside_grid(an2) and self.is_inside_grid(an1):
                            antinodes.add(an1)
                            antinodes.add(an2)
                        elif self.is_inside_grid(an1):
                            antinodes.add(an1)
                        elif self.is_inside_grid(an2):
                            antinodes.add(an2)
                        factor+=1
                        an1 = self.find_possible_antinode_pos(pos_a1, pos_a2, factor)[0]
                        print(factor)
                        an2 = self.find_possible_antinode_pos(pos_a1, pos_a2, factor)[1]
        return len(antinodes)

if __name__ == "__main__":
    filepath = "D:\\ACADS\\AOC\\day8\\input.txt"
    sol2 = Solution2(filepath)
    print(sol2.find_all_harmonic_antinodes())
            
