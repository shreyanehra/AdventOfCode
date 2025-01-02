import re
class Solution:

    def __init__(self, filepath):
        self.filepath = filepath

    def process_file(self):
        with open(self.filepath, 'r') as f:
            content = f.read()
            return content
        
    def make_list_muls(self, content):
        #content is a huge string now for part 1
        #content is a single element list for part 2
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, content)

        return matches
    
    
    def make_lists_mul_do_dont(self, content):
        patterns = [r"mul\((\d{1,3}),(\d{1,3})\)",
                    r"do\(\)",
                    r"don\'t\(\)"]

        '''
        idea is to iterate through the content and add every occurence of 
        mul(), do() and don't() in a list which is initially not sorted .
        after that the list is sorted.
        '''

        matches = []
        for pattern in patterns:
            for match in re.finditer(pattern, content):
                matches.append((match.group(), match.start()))
        
        matches.sort(key = lambda x: x[1])

        return matches
                

           
    def sum_of_products(self, matches):
        sum_prods = 0
        for index,pair in enumerate(matches):
            sum_prods += int(pair[0])*int(pair[1])
        return sum_prods
    
    def sum_prods_do_dont(self, matches):
        sum_prods =0
        
        allowed = True
        
        '''
        allowed acts as a switch, is off when the index is between occurences of dont() and do() 
        in that order. All allowed mul pairs are multiplied and added to sum_prods
        :return : sum_prods -> sum of products of allowed muls
        '''
        
        index = 0
        while(index < len(matches)):
            if (matches[index][0]!="do()" and matches[index][0]!="don't()" ):
                if(allowed is True):                   
                    pair = self.make_list_muls(matches[index][0])
                    sum_prods += int(pair[0][0])*int(pair[0][1])
            elif matches[index][0]=="don't()":
                allowed=False
            else :
                allowed=True
            index+=1        

        return sum_prods

if __name__ == "__main__":
    filepath = "D:\\ACADS\\AOC\\2024\\day3\\input.txt"
    sol = Solution(filepath)
    print(sol.sum_prods_do_dont(sol.make_lists_mul_do_dont(sol.process_file())))
