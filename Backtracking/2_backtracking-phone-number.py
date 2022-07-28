# given a string, print all possible strings which do not contain 'AB' as a substring

# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.
#
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.

# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

def letterCombinations(digits: str):
    if len(digits) == 0: return []

    lookup = {
        "2": "abc", "3": "def",
        "4": "ghi", "5": "jkl", "6": "mno",
        "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    combinations = []

    def backtrack(pos, comb):
        # if len of comb is same as len of digits, the comb is complete
        if len(comb) == len(digits):
            combinations.append("".join(comb))
            return  # Backtract

        keys = lookup[digits[pos]]
        for char in keys:
            comb.append(char)
            backtrack(pos + 1, comb)
            comb.pop()

    backtrack(0, [])
    return combinations

print(letterCombinations(digits='237'))