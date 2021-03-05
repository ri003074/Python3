def sherlockAndAnagrams(s):
    s_list = list(s)
    print(s_list)

    result = 0
    for i in range(len(s_list)):
        for j in range(i + 1, len(s_list)):
            s_word = "".join(s_list[i:j])
            s_target = "".join(s_list[i + 1 :])
            s_target_inv = s_target[::-1]
            print("search word", s_word)
            print("search target", s_target_inv)
            result += s_target_inv.count(s_word)
            print("result=", result)

    print(result)
    pass


# sherlockAndAnagrams("abba")
# sherlockAndAnagrams("abcd")
# sherlockAndAnagrams("cdcd")
sherlockAndAnagrams("kkkk")
# sherlockAndAnagrams("ifailuhkqq")
