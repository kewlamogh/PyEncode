class EncodeJS{
    constructor() {
        this.textToNumber = {};
        this.numberToText = {};
    }

    addKeyToTextToNumber(keyName, keyVal) {
        this.textToNumber[keyName.toLowerCase()] = keyVal;
        this.textToNumber[keyName.toUpperCase()] = keyVal;

        this.numberToText[keyVal.toString()] = keyName;
    }

    encode(txt) {
        let chars = txt.split('');
        let encoded = [];
        for (var i in chars) {
            encoded.push(this.textToNumber[chars[i]]);
        }
        return (encoded.join(':'));
    }

    decode(txt) {
        let letters = txt.split(':');
        let decoded = [];
        for (var i in letters) {
            decoded.push(this.numberToText[letters[i]]);
        }

        return (decoded.join(''));
    }

    initialize() {
        this.addKeyToTextToNumber('a', 2);
        this.addKeyToTextToNumber('b', 3);
        this.addKeyToTextToNumber('c', 4);
        this.addKeyToTextToNumber('d', 5);
        this.addKeyToTextToNumber('e', 6);
        this.addKeyToTextToNumber('f', 7);
        this.addKeyToTextToNumber('g', 8);
        this.addKeyToTextToNumber('h', 9);
        this.addKeyToTextToNumber('i', 10);
        this.addKeyToTextToNumber('j', 11);
        this.addKeyToTextToNumber('k', 12);
        this.addKeyToTextToNumber('l', 13);
        this.addKeyToTextToNumber('m', 14);
        this.addKeyToTextToNumber('n', 15);
        this.addKeyToTextToNumber('o', 16);
        this.addKeyToTextToNumber('p', 17);
        this.addKeyToTextToNumber('q', 18);
        this.addKeyToTextToNumber('r', 19);
        this.addKeyToTextToNumber('s', 20);
        this.addKeyToTextToNumber('t', 21);
        this.addKeyToTextToNumber('u', 22);
        this.addKeyToTextToNumber('v', 23);
        this.addKeyToTextToNumber('w', 24);
        this.addKeyToTextToNumber('x', 25);
        this.addKeyToTextToNumber('y', 26);
        this.addKeyToTextToNumber('z', 1);
        this.addKeyToTextToNumber(' ', '-');
        this.addKeyToTextToNumber('.', '🤘')
        this.addKeyToTextToNumber('!', '🏴')
        this.addKeyToTextToNumber('?', '👨‍💻')
    }
}


let encoder = new EncodeJS();
let lolEncoded = encoder.encode('Hey my name is Jamboni Quick, boi!');
let lolDecoded = encoder.decode(lolEncoded);

console.log('Encoded is: '+lolEncoded);
console.log('Decoded is: '+lolDecoded);
