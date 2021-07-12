# PyEncode - your super secure, simple to use, cipher!
## Download
Check out (or create a pull request) this repository and move `encode.py` to your program's folder.  


## Getting started

Import pyencode,
```py
import pyencode
myEncoder = pyencode.EncodePy()
```
Alternatively,
```py
from pyencode import EncodePy
myEncoder = EncodePy()
```

## Functions
#### Note: for example purposes, the instance of the `EncodePy` class will be `myEncoder`

|Function|Purpose|
---|---
|`myEncoder.encode(text)`|Encodes text and returns value in encoded format|
|`myEncoder.decode(encodedText)`|Decodes encoded text.|
|`myEncoder.addKeyToTextToNumber(keyname, keycode)`|Adds key to encode algorithm (e.g., more characters can be allowed like 👨 or 🤘)|
|`myEncoder.initialize()`|Is called during the `__init__` function, sets up the foundation for the encode algorithm. Useful when accidentally overwriting a default when using `addKeyToTextToNumber`. Does not delete extra characters.|
