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
|`myEncoder.addKeyToTextToNumber(keyname, keycode)`|Adds key to encode algorithm (e.g., more characters can be allowed like 👨 or 🤘)|
|`myEncoder.initialize()`|Is called during the `__init__` function, sets up the foundation for the encode algorithm. Useful when accidentally overwriting a default when using `addKeyToTextToNumber`. Does not delete extra characters.|
