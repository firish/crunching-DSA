def helper(s, word):
    print("string ::: " + str(s), end=", ")
    print("word ::: " + str(word), end="\n\n")
    if not s:
        res.append(word)
    else:
        if s[0] == "{":
            i = s.find("}")
            for letter in s[1:i].split(','):
                helper(s[i + 1:], word + letter)
        else:
            helper(s[1:], word + s[0])



res = []
helper("{a,b}c{d,e}f", "")
res.sort()
print(res)