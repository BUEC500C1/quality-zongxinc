def arabic_roman(num):
    table = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [100, 'C'], [90, 'XC'], 
    [50, 'L'], [40, 'XL'],[10, 'X'], [9, 'IX'], [5, 'V'], [4, 'IV'], [1, 'I']]
    res = ''
    if num > 9999:
        return 'too big'
    for unit, roman in table:
        res += roman * (num//unit)
        num %= unit
    return res
