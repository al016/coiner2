# -*- coding: utf-8 -*-
from src.models.user import User
from src.models.wallet import Wallet
from src.models.category import Category
from src.exceptions import RegistrationError

class MainClass(object): 
  def __init__(self):
    pass
  
  def login(self):
    username = raw_input("Имя пользователя: ")
    try:
        user = User.db_get(username=username)
    except Exception:
        print 'такого пользователя нет'
    password = raw_input("Пароль: ")
    user.login(password)
    return user

  def registration(self):
      """
      Возвращает пользователя.
      Либо в случае неудачи raise RegistraionError

      """

      def get_password():
          """
          Ввести пароль и подтвердить его.
          Либо возвращает 1, если не получилось.
          Либо финальный пароль

          """
          password = raw_input("Пароль: ")
          repeat_password = raw_input("Повторите пароль: ")
          if password != repeat_password:
              print 'Пароли не совпадают'
              print '1 - Повторить ввод паролей'
              print 'Любой символ - выход'
              choice = raw_input("Ваш выбор: ")
              if choice == '1':
                  get_password()
              else:
                  return -1
          else:
              return password
        

      try:
          print 'Регистрация'
          username = raw_input("Имя пользователя: ")

          password = get_password()
          if password == -1:
              raise RegistrationError('Не зарегистрирован')

          name = raw_input(
              "Введите имя (не обязательно - нажать Enter): "
          ) or None

          email = raw_input(
              "Введите Email (не обязательно - нажать Enter): "
          ) or None  

          if (email is not None) and ("@" not in email or "." not in email):
              raise ValueError('Некорректный формат Email-а')

          user = User(
              username=username,
              password=password,
              name=name,
              email=email
          )
          return user
     
      except ValueError as err:
          print 'Ошибка при регистрации:', err.message
          print '1 - Повторить регистрацию'
          print 'Любой символ - выйти'
          choice = raw_input("Выбор: ")
          if choice == '1':
              return self.registration()
          else:
              raise RegistrationError("Ошибка при регистрации")

  def start(self):
      print 'Привет!'
      print 'Что вы хотите сделать: '
      print '1 - Войти\n2 - Зарегистрироваться'
      print 'Любой символ - выйти'
      choice = raw_input('Ваш выбор: ')

      if choice == '1':
          pass
      elif choice == '2':
         try:
              user = self.registration()
              print 'Пользователь {0} успешно зарегистрирован'.format(
                user.username
              )
              return user
         except RegistrationError as err: 
              print 'Ошибка регистрации ', err.message
              self.start()
      else:
          exit()
               



if __name__ == '__main__':
    user = MainClass()
    current_user = user.start()