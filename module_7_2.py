from fileinput import close


def custom_write(file_name, strings):
    count = 1
    string_positions={}
    file = open(file_name,'w',encoding='utf8')
    for str in strings:
        curs = file.tell()
        key=(count,curs)
        file.write(str +'/n')
        string_positions[key]= str
        count+=1
    file=close()
    return string_positions








info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)