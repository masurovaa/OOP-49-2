Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
Geeks.pop('bag')
Geeks['address'] ='Ибраимова 103, БЦ Victory'
Geeks['phone:'] = 'W/A_996507052018, Тел.: 0777052018, 0557052018'
Geeks['instagram'] = '@geeks.edu'
Geeks1 = ['Основы программирования', 'UX/UI дизайн', '1C разработчик', 'Проектный менеджер']
Geeks['courses'] = list(set(Geeks['courses'] + Geeks1))
Geeks['data_of_foundation'] = '2018'
print(f'количество курсов: {len(Geeks["courses"])}')

for key, value in Geeks.items():
     print(f'{key}: {value}')































