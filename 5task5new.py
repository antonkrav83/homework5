def high_2(number):
  if (not (number & (number - 1))):
     return number
  return 0x8000000000000000 >> (64 - number.bit_length())
number = int(input('Введите цифру: '))
print(high_2(number))


