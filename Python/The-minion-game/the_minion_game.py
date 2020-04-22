def minion_game(string):
    vowel = ('A','E','I','O','U')
    stuart_score = 0 #consonants
    kevin_score = 0 #vowels

    string_len = len(string)

    for i in range(0,string_len):
        if string[i] in vowel:
            kevin_score += string_len-i
        else:
            stuart_score += string_len-i

    if kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    if stuart_score > kevin_score:
        print("Stuart {}".format(stuart_score))
    if kevin_score==stuart_score:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)