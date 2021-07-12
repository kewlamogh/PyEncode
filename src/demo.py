import pyencode
class Demo():
  def __init__(self):
    self.encoder = pyencode.EncodePy()
    self.testSubject = ''
  def example1(self):
    self.testSubject = 'abcdefghijklmnopqrstuvwxyz1234567890-:.,?!'
    print(self.encoder.encode(self.testSubject) + ' is the Encoded text.')
    print(self.encoder.decode(self.encoder.encode(self.testSubject)) + ' is the Decoded text.')
  def example2(self):
    self.testSubject = 'This is super classified message - for only Bob and I.'
    print('Encoded: '+self.encoder.encode(self.testSubject))
    print('Decoded: '+self.encoder.decode(self.encoder.encode(testSubject)))
