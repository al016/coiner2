# -*- coding: utf-8 -*-
import hashlib

from models.user import User
from models.category import Category
from models.wallet import Wallet
import main

class TestUserCase(object):
	"""
	Тестируем модель Пользователя
	"""

	def SetUp(self):
		"""
		Запускается в начале каждого теста,
		создает пользователя для тестирования
		"""
		self.real_name, self.real_password = 'test User', 'password1234'
		self.user = User(self.real_name, self.real_password)
		print self.user.username

	def test_user_regionstration(self):
		"""
		Провереряет равенство пароля класса
		User с real_password
		"""
		self.SetUp()
		print 'test1'
		assert self.user.username == self.real_name
		assert not self.user.is_login
		assert self.user.password == hashlib.md5(self.real_password).hexdigest()

	def test_user_login_success(self):
		"""
		Проверка статуса входа
		"""
		print 'test2'

		self.SetUp()
		self.user.login(self.real_password)
		assert self.user.is_login

	def test_user_login_fail(self):
		"""
		Проверка статуса [не]входа
		"""
		print 'test3'
		self.SetUp()
		self.user.login(self.real_password + 'DSzz')
		assert not self.user.is_login

	def test_user_logout(self):
		"""
		Проверяет функцию выхода из профиля
		"""
		print 'test4'
		self.SetUp()
		try:
			self.user.logout()
			raise AssertionError
		except Exception as err:
			assert isinstance(err, ValueError)
		self.user.login(self.real_password)
		assert self.user.is_login
		self.user.logout()
		assert not self.user.is_login

	def run_all_test(self):
		"""
		Запускает все тесты
		"""
		self.SetUp()
		self.test_user_regionstration()
		self.test_user_login_success()
		self.test_user_login_fail()
		self.test_user_logout()


# TODO: Homework
class TestCategoryCase(object):
	def SetUp(self):
		"""
		Запускается в начале каждого теста,
		создает пользователя для тестирования
		"""
		self.name, self.total_money = 'test Category', 1000000
		self.category = Category(self.name, self.total_money)
	
	def test_add_money(self):
		"""
		Проверяет функцию пополнения баланса
		"""
		self.SetUp()
		before_balance = self.category.balance
		self.category.add_money(666)
		assert self.category.balance == before_balance + 666

	def test_move_money_from_cat_to_cat(self):
		self.SetUp()
		test_category = Category("test Catogory 2", 500)
		self.category.move_money(300000, test_category)
		assert self.category.balance == 700000
		assert test_category.balance == 300500
		
  	def test_move_money_from_cat_to_wallet(self):
		self.SetUp()
		test_wallet = Wallet("test Wallet", 500)
		self.category.move_money(300000, test_wallet)
		assert self.category.balance == 700000
		assert test_wallet.balance == 300500

	def run_all_test(self):
		"""
		Запускает все тесты
		"""
		self.test_add_money()
		self.test_move_money_from_cat_to_cat()
		self.test_move_money_from_cat_to_wallet()


# TODO: Homework
class TestWalletCase(object):
	def SetUp(self):
		"""
		Запускается в начале каждого теста,
		создает пользователя для тестирования
		"""
		self.name, self.total_money = 'test Wallet', 1000000
		self.wallet = Wallet(self.name, self.total_money)

	def test_add_money(self):
		"""
		Проверяет функцию перемещения денег
		"""
		self.SetUp()
		self.wallet.add_money(666)
		assert self.wallet.balance == 1000666

	def test_move_money_from_wal_to_wal(self):
		"""
		Проверяет функцию пополнения баланса
		"""
		self.SetUp()
		test_wallet = Wallet("wallet 2", 400)
		self.wallet.move_money(300000, test_wallet)
		assert self.wallet.balance == 700000
		assert test_wallet.balance == 300400
    
	def test_move_money_from_wal_to_cat(self):
		"""
		Проверяет функцию пополнения баланса
		"""
		self.SetUp()
		test_cat = Category("category", 400)
		self.wallet.move_money(300000, test_cat)
		assert self.wallet.balance == 700000
		assert test_cat.balance == 300400

	def run_all_test(self):
		"""
		Запускает все тесты
		"""
		self.test_add_money()
		self.test_move_money_from_wal_to_wal()
		self.test_move_money_from_wal_to_cat()


class TestMain(object):
	"""
	Тестируем клиент пользователя
	"""

	def SetUp(self):
		"""
		Запускается в начале каждого теста,
		создает пользователя для тестирования
		"""
		self.real_name, self.real_password = 'test User', 'password1234'
		self.user = User(self.real_name, self.real_password)
		print self.user.username

if __name__ == '__main__':
	TestUserCase().run_all_test()
	TestCategoryCase().run_all_test()
	TestWalletCase().run_all_test()