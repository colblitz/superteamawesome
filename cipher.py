# Constants
alphabet = "abcdefghijklmnopqrstuvwxyz"

# Init
numberDict = {}
for i in xrange(26):
    numberDict[alphabet[i]] = i
    numberDict[alphabet[i].upper()] = i
    
phoneDict = {}
for c in ['a', 'b', 'c']: phoneDict[c] = 2
for c in ['d', 'e', 'f']: phoneDict[c] = 3
for c in ['g', 'h', 'i']: phoneDict[c] = 4
for c in ['j', 'k', 'l']: phoneDict[c] = 5
for c in ['m', 'n', 'o']: phoneDict[c] = 6
for c in ['p', 'q', 'r', 's']: phoneDict[c] = 7
for c in ['t', 'u', 'v']: phoneDict[c] = 8
for c in ['w', 'x', 'y', 'z']: phoneDict[c] = 9
for c in phoneDict.keys():
    phoneDict[c.upper()] = phoneDict[c]
    
caesarDict = {}
for i in xrange(26):
    shifted = alphabet[i:] + alphabet[:i]
    shiftedUpper = shifted.upper()
    caesarDict[shifted[0]] = shifted
    caesarDict[shiftedUpper[0]] = shiftedUpper

# Methods
def numberToLetter(n, indexed = 1):
    return map(lambda c: alphabet[(c-indexed) % 26], n)

def letterToNumber(s, indexed = 1):
    return map(lambda c: numberDict[c] + indexed if c in numberDict else c, s)

def letterToPhone(s):
    return map(lambda c: phoneDict[c] if c in phoneDict else c, s)

def caesar_shift(s, n):
    return ''.join(map(lambda c: caesarDict[c][n%26] if c in caesarDict else c, s))

def caesar(s):
    for i in xrange(26):
        print "%2d: %s" % (i, caesar_shift(s, i))


