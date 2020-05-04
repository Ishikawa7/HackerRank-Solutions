def merge_the_tools(string, k):
    string_len = len(string)
    tmp = ""
    for i in range(0,string_len):
        if string[i] not in tmp:
            tmp = tmp + string[i]
        if (i+1) % k == 0:
            print(tmp)
            tmp=""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)