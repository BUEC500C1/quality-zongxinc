def arabic_roman(num):
    table = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], 
    [50, 'L'], [40, 'XL'],[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
    res = ''
    for unit, roman in table:
        res += roman * (num/unit)
        num %= unit
    return res

for i in 1,4,9,16,25,49,81,1963,2015:
    print i, arabic_roman(i)
