MAX_CHARS = 256

def check(string1, string2):
    m = len(string1)
    n = len(string2)

    if m != n:
        return 0

    marked = [False] * MAX_CHARS

    map = [-1] * MAX_CHARS

    for i in range(n):

        if map[ord(string1[i])] == -1:

            if marked[ord(string2[i])] == True:
                return 0

            marked[ord(string2[i])] = True

            map[ord(string1[i])] = string2[i]

        elif map[ord(string1[i])] != string2[i]:
            return 0

    return 1


a = "wfca"
b = "yssy"
print(check(a, b))
