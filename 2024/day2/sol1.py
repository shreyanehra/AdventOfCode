class solution:

    def __init__(self, file_path):
        self.file_path = file_path

    def process_file(self):
        '''
        reads the file data and makes a list element for each report
        :return : arrays with reports
        '''
        with open(self.file_path, 'r') as file:
            content = file.read().strip().split("\n")


        for index, report in enumerate(content):
            report = (report.strip().split(" "))
            
            for index2 in range(len(report)):
                report[index2] = int(report[index2])
            
            content[index] = report
        
        return content
    
    def find_safe_reports(self, content):
        '''
        :param: list of lists containing all reports
        :return : num of safe lists
        '''
        safe_reports = 0
        
        for index, report in enumerate(content):
            i = 0
            dec = True
            while i<len(report)-1 and (report[i+1]>report[i]):
                dec = False
                if (report[i+1]-report[i])>=1 and (report[i+1]-report[i])<=3:
                    i+=1
                else : break
            if i==len(report)-1 :  safe_reports+=1
            i=0
            while (dec is not False) and i<len(report)-1 and (report[i+1]<report[i]):
                if (report[i]-report[i+1])>=1 and (report[i]-report[i+1])<=3:
                    i+=1
                else : break
            if i==len(report)-1 :  safe_reports+=1

        return safe_reports 
    
    def isSafe(self, report):
        i = 0
        dec = True
        while i<len(report)-1 and (report[i+1]>report[i]):
            dec = False
            if (report[i+1]-report[i])>=1 and (report[i+1]-report[i])<=3:
                i+=1
            else : break
        if i==len(report)-1 :  return 1
        i=0
        while (dec is not False) and i<len(report)-1 and (report[i+1]<report[i]):
            if (report[i]-report[i+1])>=1 and (report[i]-report[i+1])<=3:
                    i+=1
            else : break
        if i==len(report)-1 :  return 1      

        return -1
        

    
    def safe_reports_dampner(self, content):
        # MISSING ON 11 USE CASES 
        '''
        safe lists are lists that are either strictly inc or strictly dec and each element
          of list should differ with its's adjacent by 1,2,3.
          with dampening, lists that on removal of one element become safe are aso safe_lists
        :param: list of lists containing all reports
        :return : num of safe lists
        '''
        outs=0
        end_pures = 0
        pure=0
        safe_reports_dampened = 0
        #make an array that stores differences of all the reports
        for index, report in enumerate(content):

            list_of_diff = [0]*(len(report)-1)
            for index2 in range(len(report)-1):
                list_of_diff[index2]=report[index2+1]-report[index2]
            
            positives = 0
            negatives = 0
            outliers = 0
            
            diff_outlier_index = None
            i = 0
            sum_p = 0
            while (i<len(list_of_diff)):
                if list_of_diff[i]>0:
                    positives+=1
                    

                    if list_of_diff[i]>3:
                        outliers+=1
                        diff_outlier_index = i


                       
                elif list_of_diff[i]<0:
                    negatives+=1
                    if list_of_diff[i]<-3:
                        outliers+=1
                        diff_outlier_index = i
                        
                       # print(f"index {i} and {diff_outlier_index}")
                else:
                    outliers+=1 #when zeroes 
                    diff_outlier_index = i
                    
                    #print(f"index {i} and {diff_outlier_index}")
                i+=1
                

            if outliers>1:
                outs+=1
                print(f"From outs {list_of_diff} and index outlier : {diff_outlier_index} and outliers : {outliers}")
                
                continue #break while loop, can't be safe if more than 1 zero        

            if outliers==1:
                if (diff_outlier_index==0 or diff_outlier_index==len(list_of_diff)-1):
                    
                    if (positives==len(list_of_diff) or negatives==len(list_of_diff)):
                       # print(f"{list_of_diff} and index outlier : {diff_outlier_index} and outliers : {outliers}")
                        safe_reports_dampened+=1
                        end_pures+=1
                    
                else:
                    new_diff= list_of_diff[diff_outlier_index]+list_of_diff[diff_outlier_index+1]

                    if positives>=(len(list_of_diff)-1) and new_diff<=3 and new_diff>=1:
                        safe_reports_dampened+=1
                    if negatives>=(len(list_of_diff)-1) and new_diff>=-3 and new_diff<=-1:
                        safe_reports_dampened+=1
            if outliers==0:
                if positives==len(list_of_diff) or negatives==len(list_of_diff):
                    pure+=1
                    safe_reports_dampened+=1
                
                if (positives==len(list_of_diff)-1 and negatives==1) or (negatives==len(list_of_diff)-1 and positives==1):
                   # print(f"In one impure {list_of_diff} and index outlier : {diff_outlier_index} and outliers : {outliers}")
                    safe_reports_dampened+=1


            
        print(pure)
        print(f"end pures : {end_pures}")
        print(len(content))
        print(f"outs : {outs}")
        return safe_reports_dampened


    def brute_force_damp(self, content):
        '''
        using brute force
        :param : 
        :return : 
        '''
        safe_damps = 0
        for index, report in enumerate(content):
            if self.isSafe(report)==1:
                safe_damps+=1
            else:
                for index2,level in enumerate(report):
                    new_report = report.copy()
                    new_report.pop(index2)
                    if self.isSafe(new_report)==1:
                        safe_damps+=1
                        break

        return safe_damps   
        

                    
if __name__ == "__main__":
    sol = solution("D:\\ACADS\\AOC\\2024\\day2\\input_beby.txt")
    print(sol.brute_force_damp(sol.process_file()))
    
