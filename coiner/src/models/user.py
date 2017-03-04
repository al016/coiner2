# -*- coding: utf-8 -*-
import hashlib
from errors import DoesNotExist


class User(object):
	def __init__(self, username, password, name=None, email=None):
		"""
		Конструктор класса

		:param username: Имя пользователя
		:type username: str
		:param password: Пароль
		:type password: str
		:param name: Имя
		:type name: str
		:param email: Email
		:type email: str
		:return: None
		:rtype: None
		"""
		self.username = username
		self.password = self._hash_password(password)
		self.name = name
		self.email = email
		self.is_login = False

	def _check_password(self, real_password):
		"""
		Провереряет равенство пароля класса
		User с real_password

		:param real_password: Пароль
		:type real_password: str
		:return: True or False
		:rtype: Bool
		"""
		return hashlib.md5(real_password.encode()).hexdigest() == self.password

	@staticmethod
	def _hash_password(real_password):
		"""
		Шифрует пароль

		:param real_password: Пароль
		:type real_password: str
		:return: Pfibahjdfyysq real_passwor
		:rtype: str
		"""
		return hashlib.md5(real_password.encode()).hexdigest()

	def login(self, real_password):
		"""
		Вход в профиль

		:param real_password: Пароль
		:type real_password: str
		:return: False or (True or False)
		:rtype: Bool
		"""
		if self.is_login:
			print "You already logged in"
			return False
		self.is_login = self._check_password(real_password)
		if self.is_login:
			print 'You have succefully logged id'
		else:
			print 'Not correct password'
		return self.is_login

	def logout(self):
		"""
		Выход из профиля
		"""
		if self.is_login: 
			self.is_login = False
		else:
			raise ValueError("Cannon log out. You not logged in")
			
	@classmethod
	def db_all(cls):
		"""
		return [User(), User(), User()]
		"""
		pass
    
	@classmethod
	def db_filter(cls, **kwargs):
		"""
		Возвращает отфильтрованный список пользователей
		return [User(), User(), User()]
		User.db_filter(username='test', email='em@em.ru', dsadas=21)
		{'username': 'test', 'email': 'em@em.ru', 'dsadas': 21}
		"""
		pass
    
	@classmethod
	def db_get(cls, **kwargs):
		"""
		Возвращает лишь одно пользователя,
		удовлетворяющего критериям фильтра в kwargs,
		либо если такого пользователя нет или их больше,
		чем один, то raise DatabaseError
		"""
		if len(kwargs) == 0:
			raise ValueError('Нужен хотя бы один параметр для поиска!')
       
		with open(cls.path_to_db, 'r') as f:
			fields = f.readline().strip().split(',')
			k = set(kwargs.keys()) 
			if k > set(fields):
				raise ValueError('Not correct params')

			for line in f.readlines():
				user = line.strip().split(',')
				for ind, field in enumerate(user):
					if field == 'NULL':
						user[ind] = None
					flag = False
					data = dict(zip(fields, user))
					for key, value in kwargs.items():
						if data[key] != value:
							flag = True
							break
					if flag:
						continue
					user = cls(**data)
					return user
				raise DoesNotExist('Пользователь не существует')
    
	@classmethod
	def db_create(cls, username, ):
		user = cls(**kwargs)
		with open(cls.path_to_db, 'ra') as f:
			fields = f.readline().strip().split(',')
			insert_line = []
			for field in fields:
				insert_line.append(getattr(user, field) or 'NULL')
				f.write(','.join(insert_line))