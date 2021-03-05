def minion_game(string):
    vowel = ["A", "E", "I", "O", "U"]
    S = 0
    K = 0
    for i in range(len(string)):
        if string[i] in vowel:
            K += len(string) - i
        else:
            S += len(string) - i

    if S > K:
        print("Stuart" + " " + "%d" % S)
    elif K > S:
        print("Kevin" + " " + "%d" % K)
    else:
        print("Draw")


s = "BANANA"
minion_game(s)


""" answer
S = raw_input().strip()
S_length = len(S)
player1, player2 = 0,0

for i in xrange(S_length):
    if S[i] in "AEIOU":
        player1 += S_length - i
    else:
        player2 += S_length - i

if player1 > player2:
    print "Kevin", player1
elif player1 < player2:
    print "Stuart", player2
else:
    print "Draw"
"""
