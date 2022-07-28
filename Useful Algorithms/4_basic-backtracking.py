# use backtracking to find all permutations of a string

permutations = []
string = 'abcx'
combination = ''

def permute(s, combination, permutations):
    if len(s) == 0:
        permutations.append(combination)
        print(permutations)
        return permutations
    else:
        for i in range(len(s)):
            char = s[i]
            left = s[:i]
            right = s[i+1:]
            rest = left + right
            print(s, char, rest, combination+char)
            permute(rest, combination+char, permutations)


permute(string, combination, permutations)
print(permutations)


