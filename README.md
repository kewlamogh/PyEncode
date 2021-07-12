# PyEncode - your super secure and simple to use cipher!
## Download
Check out (or create a pull request) this repository and move `encode.py` to your program's folder.  


## Getting started

Import pyencode,
```py
import pyencode
myEncoder = pyencode.EncodePy() #getting the EncodePy class from the module
```
Alternatively,
```py
from pyencode import EncodePy
myEncoder = EncodePy() # EncodePy class
```

## Functions
#### _Note: for example purposes, the instance of the `EncodePy` class will be `myEncoder`_

|Function|Purpose|
---|---
|`myEncoder.encode(text)`|Encodes text and returns value in encoded format|
|`myEncoder.decode(encodedText)`|Decodes encoded text.|
|`myEncoder.addKeyToTextToNumber(keyname, ciphered)`|Adds key to encode algorithm (e.g., more characters can be allowed like 👨 or 🤘)|
|`myEncoder.initialize()`|Is called during the `__init__` function, sets up the foundation for the encode algorithm. Useful when accidentally overwriting a default when using `addKeyToTextToNumber`. Does not delete extra characters.|

## Characters supported
A-Za-z0-9?.!-_@:,;
To add more characters, use the `addKeyToTextToNumber(keyname, ciphered)` function. If your message contains an unsupported character, then you will get an error in the terminal/console.

## A quick demo 
For a simple demo of this, just download the `demo.py` file and run it (and do look at the source code).


## Disclaimer: 
This does not have protection. If someone (who isn't supposed to get the ciphered `str`) gets it, they will be able to decode it using the `decode` function. However this rarely happens unintentionally since most messaging platforms (e.g., Google Chat or WhatsApp) have DM systems. I did not implement this in my module since this is mostly for in-program use (e.g., when you don't want the client to `console` hack the cheat codes of the game). As a result, it is ill-advised to use this for really confidential stuff, like credit card numbers and more.
