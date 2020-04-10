import os, sys


class Entity:
	def __init__(self, name, alias=None, category=None, **properties):
		'''
		category:	category
		properties: features
		'''
		self._name = name
		self._alias = alias
		self._category = category
		self._properties = properties

	@property
	def name(self):
		return self._name

	@property
	def alias(self):
		return self._alias

	@alias.setter
	def alias(self, alias):
		self._alias = alias

	@property
	def category(self):
		return self._category

	@category.setter
	def category(self, category):
		self._category = category

	@property
	def properties(self):
		return self._properties

	@property
	def property_names(self):
		return self._properties.keys()

	@property
	def property_values(self):
		return self._properties.values()

	def hasProperty(self, prop):
		return prop in self._property.keys()

	def isIdentityOf(self, en):
		if isinstance(en, self.__class__):
			diff = True
			if self._name == en.name and self._alias == en.alias and self._category == en.category:
				# check properties
				for key, value in self._properties.items():
					if en.properties[key] != value:
						return False
					else:
						pass
				return True
			else:
				return False
		else:
			return False


if __name__ == '__main__':
	e1 = Entity('name1', {'1':1,'2':2,'3':3})
	e2 = Entity('name2', {'1':1,'2':2,'3':3})
	e3 = Entity('name1', {'1':1,'2':2,'3':4})
	e4 = Entity('name1', {'1':1,'2':2,'3':3})
	
	print('e1 == e2: ', e1.isIdentityOf(e2))
	print('e1 == e3: ', e1.isIdentityOf(e3))
	print('e1 == e4: ', e1.isIdentityOf(e4))
	print(e1.property_names)
	print(e1.property_values)
