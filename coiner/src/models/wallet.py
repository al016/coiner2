# -*- coding: utf-8 -*-
from mixins import Keeper


class Wallet(Keeper):
	"""
	Класс кошелька, наследуемый от класса Keeper
	"""
	def __init__(self, *args, **kwargs):
		"""
		Конструктор класса, принимает содержимое метода
		__init__() класса Keeper; идентификатор
		кошелька
		"""
		super(Wallet, self).__init__(*args, **kwargs)
		self.tag = None


	def add_money(self, *args):
		super(Wallet, self).add_money(*args)

