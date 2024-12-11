data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

letters=[x for x in data_tuple if type(x) == str]
letters.append (data_tuple[5])
letters [-2] = 'G'
letters [1] = 'c'
letters.reverse()
letters = tuple(letters)

print('Буквы:', letters)

numbers = [x for x in data_tuple if type(x) == int]
numbers.append (2)
numbers = sorted(numbers)
numbers = [number **2 for number in numbers]
numbers = tuple(numbers)

print('Цифры:', numbers)