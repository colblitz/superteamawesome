import random

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

def letterToNumber2(s, indexed = 1):
    return map(lambda c: numberDict[c] + indexed if c in numberDict else None, s)

def letterToPhone(s):
    return map(lambda c: phoneDict[c] if c in phoneDict else c, s)

def caesar_shift(s, n):
    return ''.join(map(lambda c: caesarDict[c][n%26] if c in caesarDict else c, s))

def caesar(s):
    for i in xrange(26):
        print "%2d: %s" % (i, caesar_shift(s, i))

print caesar_shift("blah hello This is a test of it's !", 5)


print caesar_shift(caesar_shift("blah hello this is a test", 6), -6)
def vigenere(m, k):
    message = ""
    i = 0
    keys = [x for x in letterToNumber2(k) if x]
    c = len(keys) - 1
    for l in m.lower():
        if l in alphabet:
            message += caesar_shift(l, keys[i])
            i = 0 if i == c else i + 1
        else:
            message += l
    return message

def devigenere(m, k):
    message = ""
    i = 0
    keys = [x for x in letterToNumber2(k) if x]
    c = len(keys) - 1
    for l in m.lower():
        if l in alphabet:
            message += caesar_shift(l, -keys[i])
            i = 0 if i == c else i + 1
        else:
            message += l
    return message
print vigenere("this is a test message To Test's ! blah .", "it's Key!")
print devigenere(vigenere("hell this is another test", "it's key!"), "it's key!")

    
def enigmaLetter(wheels, l):
    i = letterToNumber(l, 0)[0]
    for w in wheels:
        i = w[i]
    return numberToLetter([i], 0)[0]

def deenigmaLetter(wheels, l):
    i = letterToNumber(l, 0)[0]
    for w in wheels[::-1]:
        i = w.index(i)
    return numberToLetter([i], 0)[0]


def shiftWheel(l):
    return l[-1:] + l[:-1]

def enigmaShift(wheels, wheel_shifts):
    wheel_shifts += 1
    for i in xrange(len(wheels)):
        if wheel_shifts % 26**i == 0:
            wheels[i] = shiftWheel(wheels[i])

def enigma(m, w = 5, s = 0):
    wheels = []
    wheel_shifts = 0
    random.seed(s)
    for i in xrange(w):
        t = range(26)
        random.shuffle(t)
        wheels.append(t)
    message = ""
    for l in m.lower():
        if l in alphabet:
            message += enigmaLetter(wheels, l)
            enigmaShift(wheels, wheel_shifts)
        else:
            message += l
    return message

def deenigma(m, w = 5, s = 0):
    wheels = []
    wheel_shifts = 0
    random.seed(s)
    for i in xrange(w):
        t = range(26)
        random.shuffle(t)
        wheels.append(t)
    message = ""
    for l in m.lower():
        if l in alphabet:
            message += deenigmaLetter(wheels, l)
            enigmaShift(wheels, wheel_shifts)
        else:
            message += l
    return message
    

print enigma("Hello word, this is a test of it's stuff!")
print deenigma(enigma("helloworld"))
