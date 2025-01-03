class Solution:
    def __init__(self, fileRulesPath, fileUpdatesPath):
        '''
        
        '''
        self.fileRulespath = fileRulesPath
        self.fileUpdatesPath = fileUpdatesPath

    def process_files(self):
        '''
        
        '''
        with open(self.fileRulespath,"r") as file_rules:
            content_rules = file_rules.read().splitlines()
        rules_dict = {}
        for index,element in enumerate(content_rules):
            a = tuple(element.split("|"))
            content_rules[index] = (int(a[0]), int(a[1]))

            # Initialize the key with an empty set if it doesn't exist
            if int(a[1]) not in rules_dict:
                rules_dict[int(a[1])] = set()
    
            # Add the value to the set
            rules_dict[int(a[1])].add(int(a[0]))
        
        with open(self.fileUpdatesPath,"r") as file_updates:
            content_updates = file_updates.read().splitlines()
        
        for i,update in enumerate(content_updates):
            u = update.split(",")
            for j,page in enumerate(u):
                u[j]=int(page)
            content_updates[i] = u
        
        return rules_dict, content_updates
    
    def find_safe_updates(self, rules_dict, content_updates):
        sum = 0
        
        for index, update in enumerate(content_updates):
            flag = 0
            for page in range(0,len(update)):
                if update[page] not in rules_dict:
                    continue
                else :
                    for page_after in range(page+1, len(update)):
                        if update[page_after] in rules_dict[update[page]]:
                            flag+=1
            if flag==0:
                sum+=update[len(update)//2]


        return sum    
                        


if __name__=="__main__":
    filepath_rules = "D:\\ACADS\\AOC\\2024\\day5\\input_rules.txt"
    filepath_updates = "D:\\ACADS\\AOC\\2024\\day5\\input_update.txt"

    sol = Solution(filepath_rules, filepath_updates)
    rules_dict, content_updates = sol.process_files()
    print(sol.find_safe_updates(rules_dict, content_updates))
