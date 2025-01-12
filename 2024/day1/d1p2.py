#writing this as a function in solution class

from d1p1 import Solution
class Solution2:
    def __init__(self, file_path):
        self.file_path = file_path


    def similarity_score(self):

        '''
        param file1 : string containing input file location
        return : similarity_score
        '''
        sol1 = Solution(self.file_path)
        result1 = sol1.process_file()
        list1_sorted = result1[0]
        list2_sorted = result1[1]
        counter = 0
        i=0
        j=0
        similarScore = 0

        for i in range(len(list1_sorted)):
            while (list1_sorted[i]>list2_sorted[j]):
                j+=1
            if (list1_sorted[i]==list2_sorted[j]):
                while (list1_sorted[i]==list2_sorted[j]):
                    counter+=1
                    j+=1
                similarScore += list1_sorted[i]*counter    
            counter = 0   
        
        return similarScore
    


if __name__ == "__main__":
    solution2 = Solution2("D:\\ACADS\\AOC\\2024\\day1\\aoc1_input.txt")           
    
    print(solution2.similarity_score())

        

