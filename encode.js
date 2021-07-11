let textToNumber = {};
let numberToText = {};
function addKeyToTextToNumber(keyName, keyVal) {
    textToNumber[keyName.toLowerCase()] = keyVal;
    textToNumber[keyName.toUpperCase()] = keyVal;

    numberToText[keyVal.toString()] = keyName;
}

function encode(txt) {
    let chars = txt.split('');
    let encoded = [];
    for (var i = 0; i <= chars.length - 1; i++) {
        encoded.push(textToNumber[chars[i]]);
        console.log(i);
    }
    return encoded.join(':');
}

function decode(txt) {
    let letters = txt.split(':');
    let decoded = [];
    for (var i = 0; i <= letters.length - 1; i++) {
        decoded.push(numberToText[letters[i]]);
    }
    return decoded.join('');
}

function initialize() {
    addKeyToTextToNumber('a', 2);
    addKeyToTextToNumber('b', 3);
    addKeyToTextToNumber('c', 4);
    addKeyToTextToNumber('d', 5);
    addKeyToTextToNumber('e', 6);
    addKeyToTextToNumber('f', 7);
    addKeyToTextToNumber('g', 8);
    addKeyToTextToNumber('h', 9);
    addKeyToTextToNumber('i', 10);
    addKeyToTextToNumber('j', 11);
    addKeyToTextToNumber('k', 12);
    addKeyToTextToNumber('l', 13);
    addKeyToTextToNumber('m', 14);
    addKeyToTextToNumber('n', 15);
    addKeyToTextToNumber('o', 16);
    addKeyToTextToNumber('p', 17);
    addKeyToTextToNumber('q', 18);
    addKeyToTextToNumber('r', 19);
    addKeyToTextToNumber('s', 20);
    addKeyToTextToNumber('t', 21);
    addKeyToTextToNumber('u', 22);
    addKeyToTextToNumber('v', 23);
    addKeyToTextToNumber('w', 24);
    addKeyToTextToNumber('x', 25);
    addKeyToTextToNumber('y', 26);
    addKeyToTextToNumber('z', 1);
    addKeyToTextToNumber(' ', '-');
    addKeyToTextToNumber('.', '🤘')
    addKeyToTextToNumber('!', '🏴')
    addKeyToTextToNumber('?', '👨‍💻')
}

let encoded = encode('Lorem Ipsum');
console.log(encoded);
let decoded = decode(encoded);
console.log(decoded)

