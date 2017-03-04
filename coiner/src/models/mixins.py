# -*- coding: utf-8 -*-
class Keeper(object):
	def __init__(self, name, total_money=0):
		"""
		Конструктор класса

		:param name: Сумма денег
		:type name: str
		:return: None
		:rtype: None
		"""
		self.name = name
		self.__total_money = total_money

	def add_money(self, money):
		"""
		Добавляет деньги

		:param money: Сумма денег
		:type money: float
		:return: None
		:rtype: None
		"""
		self.__total_money += money

	def move_money(self, money, destination_obj):
		"""
		Переносит деньги из одного кошелька 
		в другой.

		:param money: Сумма денег
		:type money: float
		:param destination: Объект 
		:type destination: models.mixins.Keeper
		:return: None
		:rtype: None
		"""
		if money > self.__total_money:
			raise ValueError('Not enough money!')
		else:
			destination_obj.add_money(money)
			self.__total_money -= money

	@property
	def balance(self):
		return self.__total_money
