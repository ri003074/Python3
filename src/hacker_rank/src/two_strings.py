def twoStrings(s1, s2):
    for i in range(len(s2)):
        print(s1.find(s2[i]))
        if s1.find(s2[i]) >= 0:
            return "YES"

    return "NO"


def twoStrings2(s1, s2):
    # create sets of unique characters
    # and test for intersection
    print(set(s1))
    if set(s1) & set(s2):
        return "YES"
    else:
        return "NO"


print(twoStrings("ab", "abc"))
print(twoStrings2("ab", "abc"))
