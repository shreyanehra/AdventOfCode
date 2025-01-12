from d8p1 import Solution
import numpy as np
class Solution2:
    def __init__(self, filepath):
        self.filepath = filepath

    def harmonic_antinodes(self):
        sol1 = Solution(self.filepath)

        self.grid = sol1.process_file()
        self.dict_antenas = sol1.antena_types(self.grid)
        
    def is_in_grid(self, pos):
        self.rows = len(self.grid[0])
        self.cols = len(self.grid)
        if 0<=pos[0]<self.rows and 0<=pos[1]<self.cols:
            return True
        
    def fetch_vector_from_dict(self, f, nth_index_in_dict_key):
        return self.dict_antenas[f][nth_index_in_dict_key]
    def add_vec(self, f, pos, vector):
        return self.fetch_vector_from_dict(f, pos) + vector
        #assuming inputs are numpy arrays 
        
    def sub_vec(self,f, pos, vector):
        #assuming inputs are numpy arrays 
        return np.array(self.fetch_vector_from_dict(f, pos)) - np.array(vector)
    
    def calculate_distance_vector(self, f, antena1_position, antena2_position):
        vec_x = self.fetch_vector_from_dict(f,antena2_position)[0] - self.fetch_vector_from_dict(f,antena1_position)[0]
        vec_y = self.fetch_vector_from_dict(f,antena2_position)[1] - self.fetch_vector_from_dict(f,antena1_position)[1]
        return (vec_x,vec_y) 
    def find_antinodes(self):
        antinodes = set()
        self.harmonic_antinodes()
        for f in self.dict_antenas:
            num_antenas_f_particular = len(self.dict_antenas[f])
            for a1 in range(num_antenas_f_particular-1):
                for a2 in range(a1+1, num_antenas_f_particular):
                    vector = self.calculate_distance_vector(f, a1, a2)
                    an1 = self.sub_vec(f, a1, vector)
                    while self.is_in_grid(an1):
                        antinodes.add(an1)
                        vector
                        an1 = self.sub_vec(f, a1, vector)
                    an2 = self.add_vec(f, a2, vector)
                    while self.is_in_grid(an2):
                        antinodes.add(an2)
                        vector*=2
                        an2 = self.add_vec(f, a2, vector)
        return len(antinodes)

if __name__ == "__main__":
    filepath = "D:\\ACADS\\AOC\\day8\\input.txt"
    sol2 = Solution2(filepath)
    print(sol2.find_antinodes())
            
