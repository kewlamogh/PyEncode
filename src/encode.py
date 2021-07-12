class EncodePy:
  def addKeyToTextToNumber(self, keyName, keyVal):
    self.textToNumber[keyName.lower()] = keyVal
    self.textToNumber[keyName.upper()] = keyVal
    self.numberToText[str(keyVal)] = keyName
  
  def encode(self, txt):
      chars = []
      for i in txt: # welp i get an error when making a custom split func so ill do it manually, anywayss I only use it once
        chars.append(i)
      encoded = []
      for i in chars:
        encoded.append(str(self.textToNumber[i]))
      return ':'.join(encoded)

  def decode(self, txt) :
      ters = txt.split(':')
      decoded = []
      for i in ters:
        decoded.append(self.numberToText[i])
      return ''.join(decoded)

  def initialize(self):
      self.addKeyToTextToNumber('a', 2)
      self.addKeyToTextToNumber('b', 3)
      self.addKeyToTextToNumber('c', 4)
      self.addKeyToTextToNumber('d', 5)
      self.addKeyToTextToNumber('e', 6)
      self.addKeyToTextToNumber('f', 7)
      self.addKeyToTextToNumber('g', 8)
      self.addKeyToTextToNumber('h', 9)
      self.addKeyToTextToNumber('i', 10)
      self.addKeyToTextToNumber('j', 11)
      self.addKeyToTextToNumber('k', 12)
      self.addKeyToTextToNumber('l', 13)
      self.addKeyToTextToNumber('m', 14)
      self.addKeyToTextToNumber('n', 15)
      self.addKeyToTextToNumber('o', 16)
      self.addKeyToTextToNumber('p', 17)
      self.addKeyToTextToNumber('q', 18)
      self.addKeyToTextToNumber('r', 19)
      self.addKeyToTextToNumber('s', 20)
      self.addKeyToTextToNumber('t', 21)
      self.addKeyToTextToNumber('u', 22)
      self.addKeyToTextToNumber('v', 23)
      self.addKeyToTextToNumber('w', 24)
      self.addKeyToTextToNumber('x', 25)
      self.addKeyToTextToNumber('y', 26)
      self.addKeyToTextToNumber('z', 1)
      self.addKeyToTextToNumber(' ', 27)
      self.addKeyToTextToNumber('.', 28)
      self.addKeyToTextToNumber('!', 29)
      self.addKeyToTextToNumber('?', 30)
      self.addKeyToTextToNumber('1', 101)
      self.addKeyToTextToNumber('2', 102)
      self.addKeyToTextToNumber('3', 103)
      self.addKeyToTextToNumber('4', 104)
      self.addKeyToTextToNumber('5', 105)
      self.addKeyToTextToNumber('6', 106)
      self.addKeyToTextToNumber('7', 107)
      self.addKeyToTextToNumber('8', 108)
      self.addKeyToTextToNumber('9', 109)
      self.addKeyToTextToNumber('-', 99)
      self.addKeyToTextToNumber('0', 110)
      self.addKeyToTextToNumber('_', 111)
      self.addKeyToTextToNumber('@', 112)
      self.addKeyToTextToNumber(':', 113)
      self.addKeyToTextToNumber(',', 115)
  
  def __init__(self):
    self.textToNumber = {}
    self.numberToText = {}
    self.initialize()

      
