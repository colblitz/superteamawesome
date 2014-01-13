
alphabet = "abcdefghijklmnopqrstuvwxyz"
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphadict = {}
for i in xrange(26):
    alphadict[alphabet[i]] = i
    alphadict[alphabetUpper[i]] = i

# Turn into 2D lookup table
def shift(c, n):
    if c in alphabet:
        return alphabet[(alphadict[c] + n) % 26]
    elif c in alphabetUpper:
        return alphabetUpper[(alphadict[c] + n) % 26]
    else:
        return c

def caesar_shift(s, n):
    return ''.join(map(lambda x: shift(x, n), s))

def caesar(s):
    for i in xrange(26):
        print i, ": ", caesar_shift(s, i)
