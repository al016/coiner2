# -*- coding: utf-8 -*-
from mixins import Keeper


class Category(Keeper):
	"""
	Класс категории, наследуемый от класса Keeper
	"""
	def __init__(self, *args, **kwargs):
		"""
		Конструктор класса, принимает содержимое метода
		__init__() класса Keeper; идентификатор
		категории
		"""
		super(Category, self).__init__(*args, **kwargs)
		self.tag = None


	def add_money(self, *args):
		super(Category, self).add_money(*args)
