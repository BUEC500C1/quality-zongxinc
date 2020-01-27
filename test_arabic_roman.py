from arabic_roman import arabic_roman

def test():
  assert arabic_roman(1) == 'I'
  assert arabic_roman(1000) == 'too big'
  assert arabic_roman(0) == ''
  
