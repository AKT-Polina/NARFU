ls = input('Введите строку: ').split(' ') 
max_len = max([len(x) for x in ls]) 
max_word = [x for x in ls if len(x) == max_len] 
max = ''.join(max_word) 
print(f'Самое длинное слово: "{max}"') 
print(f'Длинна этого слова: {max_len}')
