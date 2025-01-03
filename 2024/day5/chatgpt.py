class Solution:
    def __init__(self, fileRulesPath, fileUpdatesPath):
        self.fileRulespath = fileRulesPath
        self.fileUpdatesPath = fileUpdatesPath

    def process_files(self):
        # Parse the rules
        with open(self.fileRulespath, "r") as file_rules:
            content_rules = file_rules.read().splitlines()
        rules_dict = {}
        for rule in content_rules:
            a, b = map(int, rule.split("|"))
            if a not in rules_dict:
                rules_dict[a] = set()
            rules_dict[a].add(b)

        # Parse the updates
        with open(self.fileUpdatesPath, "r") as file_updates:
            content_updates = [
                list(map(int, line.split(","))) for line in file_updates.read().splitlines()
            ]

        return rules_dict, content_updates

    def is_valid_update(self, update, rules_dict):
        # Check if the update satisfies the rules
        update_index = {page: idx for idx, page in enumerate(update)}  # Map page to index
        for a, after_pages in rules_dict.items():
            if a not in update_index:
                continue  # Ignore rules for pages not in the update
            for b in after_pages:
                if b in update_index and update_index[a] > update_index[b]:
                    return False  # Rule violated
        return True

    def find_safe_updates(self, rules_dict, content_updates):
        total_sum = 0
        for update in content_updates:
            if self.is_valid_update(update, rules_dict):
                middle_page = update[len(update) // 2]
                total_sum += middle_page
        return total_sum

if __name__ == "__main__":
    filepath_rules = "D:\\ACADS\\AOC\\2024\\day5\\input_rules.txt"
    filepath_updates = "D:\\ACADS\\AOC\\2024\\day5\\input_update.txt"

    sol = Solution(filepath_rules, filepath_updates)
    rules_dict, content_updates = sol.process_files()
    result = sol.find_safe_updates(rules_dict, content_updates)
    print(result)
