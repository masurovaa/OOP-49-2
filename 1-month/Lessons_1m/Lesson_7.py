""" Lambda функции. Обработка исключений."""
# Безимянное, однострочная, маленькая версия функции - def

#def plus(a, b, *args, **kwargs):
#def plus(a, b):
#    return a + b
#plus1 = (plus(8,9))
#print(plus1)

def up_first_letter(word: str) -> str:
    """Принимает слово, возвращает его с большой буквы."""
    return word.title()


def show_words(func, objects):
    for obj in objects:
       print(func,(obj))


show_words(len, ['bishkek', 'tokmok', 'kant'])
show_words(up_first_letter, ['tokmok', 'bishkek', 'kant'])
















