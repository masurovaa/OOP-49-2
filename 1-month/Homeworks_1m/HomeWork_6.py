#Функция для проверки надежности пароля.
def check_password_strength(password):
    if len(password)<6:
      return "Пароль слишком короткий. Минимум 6 символов."
    if not any(char.isdigit() for char in password):
        return "Пароль должен содержать хотя бы одну цифру."
    if not any(char.isalpha() for char in password):
      return "Пароль должен содержать хотя бы одну букву."
    return "Пароль надежный!"
password = input("Введите пароль для проверки:")
print(check_password_strength(password))



