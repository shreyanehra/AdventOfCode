#recommended to use with when opening files in python

class Solution:
    def __init__(self, file_path):
       
        self.file_path = file_path

    def process_file(self):
        """
        reads the input file, processes the data, and computes the sum of differences.
        :return: The sum of differences between sorted lists
        """
        with open(self.file_path, 'r') as input_file:
            content = input_file.read()
            # Separate by new line character
            sep_content = content.strip().split("\n")
        
        list1 = []
        list2 = []

        for pair in sep_content:
            # Split using 3 spaces and convert to integers
            sep_pair = pair.split("   ")
            list1.append(int(sep_pair[0]))
            list2.append(int(sep_pair[1]))

       
        list1_sorted = sorted(list1)
        list2_sorted = sorted(list2)
        sum_of_differences = 0
        for i in range(len(list1)):
            sum_of_differences += abs(list2_sorted[i]-list1_sorted[i])

        return list1_sorted, list2_sorted, sum_of_differences
