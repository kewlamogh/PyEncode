
textToNumber = {}
numberToText = {}
def addKeyToTextToNumber(keyName, keyVal) :
    textToNumber[keyName.toLowerCase()] = keyVal
    textToNumber[keyName.toUpperCase()] = keyVal

    numberToText[keyVal.toString()] = keyName


def encode(txt) :
    chars = txt.split('')
    encoded = []
    for i in chars:
        encoded.push(textToNumber[chars[i]])
    
    return (str(encoded)


def decode(txt) :
     ters = txt.split(':')
     decoded = []
    for (var i in ters) :
        decoded.push(numberToText[ters[i]])
    

    return (decoded.join(''))

addKeyToTextToNumber('a', 2)
addKeyToTextToNumber('b', 3)
addKeyToTextToNumber('c', 4)
addKeyToTextToNumber('d', 5)
addKeyToTextToNumber('e', 6)
addKeyToTextToNumber('f', 7)
addKeyToTextToNumber('g', 8)
addKeyToTextToNumber('h', 9)
addKeyToTextToNumber('i', 10)
addKeyToTextToNumber('j', 11)
addKeyToTextToNumber('k', 12)
addKeyToTextToNumber('l', 13)
addKeyToTextToNumber('m', 14)
addKeyToTextToNumber('n', 15)
addKeyToTextToNumber('o', 16)
addKeyToTextToNumber('p', 17)
addKeyToTextToNumber('q', 18)
addKeyToTextToNumber('r', 19)
addKeyToTextToNumber('s', 20)
addKeyToTextToNumber('t', 21)
addKeyToTextToNumber('u', 22)
addKeyToTextToNumber('v', 23)
addKeyToTextToNumber('w', 24)
addKeyToTextToNumber('x', 25)
addKeyToTextToNumber('y', 26)
addKeyToTextToNumber('z', 1)
addKeyToTextToNumber(' ', '-')
addKeyToTextToNumber('.', '🤘')
addKeyToTextToNumber('!', '🏴')
addKeyToTextToNumber('?', '👨‍💻')