"""
lambda 引数: 戻り値

def func(引数):
    return  返り値
"""


def double(n):
    return n * 2


lambda n: n * 2


lst = ["Mon", "tue", "Wed", "Thu"]


def change_words(words, func):
    for word in words:
        print(func(word))


def sample_func(word):
    return word.capitalize()


def sample_func2(word):
    return word.lower()


# change_words(l, sample_func)


change_words(lst, lambda word: word.capitalize())
change_words(lst, lambda word: word.lower())
