from arabic_roman import arabic_roman

def test():
  assert arabic_roman(1) == 'I'
  assert arabic_roman(10000) == 'too big'
  assert arabic_roman(0) == ''
  assert arabic_roman(1999) == 'MCMXCIX'
  assert arabic_roman(623) == 'DCXXIII'
  assert arabic_roman(3999) == 'MMMCMXCIX'
  assert arabic_roman(-2) == 'no negative'
