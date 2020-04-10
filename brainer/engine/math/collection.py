import os, sys
import entity
import point


class EmptySet:
	def __init__(self):
		self._members = []
		self._number_of_members = 0
		self._clusters = dict()

	@property
	def members(self):
		return self._members

	@property
	def number_of_members(self):
		return self._number_of_members

	@property
	def clusters(self):
		return self._clusters

	def append(self, obj):
		try:
			raise AttributeError("AttributeError: 'EmptySet' has no attribution 'append'")
		except Exception as err:
			print(err)
	
	def remove(self, obj):
		try:
			raise AttributeError("AttributeError: 'EmptySet' has no attribution 'remove'")
		except Exception as err:	
			print(err)

	def pop(self, idx):
		try:
			raise AttributeError("AttributeError: 'EmptySet' has no attribution 'pop'")
		except Exception as err:
			print(err)

	def isSubsetOf(self, C):
		try:
			if not isinstance(C, (self.__class__, Collection)):
				raise TypeError("TypeError: EmptySet.isSubsetOf(x): incorrect type of x")
			else:
				return True
		except Exception as err:
			print(err)

	def isProperSubsetOf(self, C):
		try:
			if not isinstance(C, (self.__class__, Collection)):
				raise TypeError("TypeError: EmptySet.isProperSubsetOf(x): incorrect type of x")
			else:
				return True
		except Exception as err:
			print(err)


class Collection:
	'''
	type limit: 1) list, tuple, dict, set, str, int, float, bool, complex
				2) Point, Entity
	'''
	type_limit = [list, tuple, dict, set, str, int, float, bool, complex, point.Point, entity.Entity]

	# collection to clusters by type
	def _divided_into_clusters_by_type(self):
		# divided into clusters
		for item in self._members:
			if type(item).__name__ not in self._clusters.keys():
				self._clusters[type(item).__name__] = []
			self._clusters[type(item).__name__].append(item)

	# update clusters
	def _update_clusters(self, opt_mode=0, target_member=None):
		'''
		opt_mode: 0 -> none
				  1 -> append
				  2 -> remove/pop
		'''
		opt_mode = opt_mode if opt_mode in [0, 1, 2] else 0
		##
		if opt_mode == 0:
			pass
		elif opt_mode == 1:
			if type(target_member) not in self._clusters.keys():
				self._clusters[type(target_member).__name__] = []
			self._clusters[type(target_member).__name__].append(target_member)
		else:
			if type(target_member) not in self._clusters.keys():
				self._clusters[type(target_member).__name__] = []
			self._clusters[type(target_member).__name__].remove(target_member)

	# redundance handle
	def _remove_redundance(self, hard=False):
		'''
		hard: do extra check for existence abnormal-typed memebers
		'''
		total_members = len(self._members)
		#
		if total_members > 0:
			if hard:
				# search for abnormal-typed members
				idx_abnormal = []
				for idx, item in enumerate(self._members):
					if type(item) not in self.type_limit:
						idx_abnormal.append(idx)
				# remove abnormal-typed members
				for i, idx in enumerate(idx_abnormal):
					self._members.pop(idx-i)

			# bubble search for identical members
			idx_redundance = []
			for idx, item in enumerate(self._members):
				for i in range(total_members-idx-1):
					if type(item) == type(self._members[i+1+idx]):
						if type(item) in self.type_limit[:-2]:
							if item == self._members[i+1+idx]:
								idx_redundance.append(idx)
						else:
							if item.isIdentityOf(self._members[i+1+idx]):
								idx_redundance.append(idx)

			# remove redundant members
			for i, idx in enumerate(idx_redundance):
				self._members.pop(idx-i)
		else:
			# do nothing
			pass

	# members & number of members
	def __init__(self, objs=[], hard=True):
		# 1) --- initialize members ---
		self._members = objs if type(objs)==list else list(objs)

		# redundance check & handling
		self._remove_redundance(hard=hard)

		# 2) --- initialize number of members ---
		self._number_of_members = len(self._members)

		# 3) --- initialize clusters ---
		self._clusters = dict()
		##
		self._divided_into_clusters_by_type()


	@property
	def members(self):
		return self._members

	@property
	def number_of_members(self):
		return self._number_of_members

	@property
	def clusters(self):
		return self._clusters

	def append(self, new_member):
		try:
			# abnormal-type check
			if type(new_member) not in self.type_limit:
				raise TypeError("TypeError: Collection.append(x): incorrect type of x")

			redundance_found = False
			# redundance check
			for item in self._members:
				if type(new_member) == type(item):
					if isinstance(new_member, tuple(self.type_limit[:-2])):
						if new_member == item:
							redundance_found = True
					else:
						if new_member.isIdentityOf(item):
							redundance_found = True
			## do update
			if not redundance_found:
				self._members.append(new_member)
				# update number of members
				self._number_of_members = len(self._members)
				# update clusters
				self._update_clusters(opt_mode=1, target_member=new_member)
		except Exception as err:
			print(err)


	def append_all(self, new_members):
		try:
			# abnormal-type check
			if not isinstance(new_members, (list, tuple)):
				raise TypeError("TypeError: Collection.append_all(self, x): incorrect type of x")
			else:
				for member in new_members:
					if type(member) not in self.type_limit:
						raise TypeError("TypeError: Collection.append_all(self, x): incorrect type of x's members")
					else:
						redundance_found = False
						for item in self._members:
							redundance_found = True if type(member)==type(item) and ((isinstance(member, tuple(self.type_limit[:-2])) and member==item) or (isinstance(member, tuple(self.type_limit[-2:])) and member.isIdentityOf(item))) else False
						## do update
						if not redundance_found:
							if isinstance(member, (EmptySet, Collection)):
								print("**** ", member.name)
							else:
								print("**** ", member)
							self._members.append(member)
							self._number_of_members += 1
							self._update_clusters(opt_mode=1, target_member=member)

		except Exception as err:
			print(err)
	
	# remove a member from collection
	def remove(self, member):
		try:
			# abnormal-type check
			if type(member) not in self.type_limit:
				raise TypeError("TypeError: Collection.remove(x): incorrect type of x")
			not_found = True
			for item in self._members:
				if isinstance(member, tuple(self.type_limit[:-2])):
					if member == item:
						self._members.remove(item)
						# update number of members
						self._number_of_members = len(self._members)
						# update clusters
						self._update_clusters(opt_mode=2, target_member=member)
						not_found = False
						break
				else:
					if member.isIdentityOf(item):
						self._members.remove(item)
						# update number of members
						self._number_of_members = len(self._members)
						# update clusters
						self._update_clusters(opt_mode=2, target_member=member)
						not_found = False
						break
			##
			if not_found:
				raise ValueError("ValueError: Collection.remove(x): x not in Collection")
		except Exception as err:
			print(err)


	# pop a member out of collection
	def pop(self, idx):
		try:
			if idx not in [i-self._number_of_members for i in range(2*self._number_of_members)]:
				raise IndexError("IndexError: pop index out of range")
			# cache member that is to be popped out
			member_to_popout = self._members[idx]
			# pop member out of collection
			self._members.pop(idx)
			# update number of members
			self._number_of_members = len(self._members)
			# update clusters
			self._update_clusters(opt_mode=2, target_member=member_to_popout)
		except Exception as err:
			print(err)


	# bilateral intersection
	def _bilateral_intersection(self, C):
		try:
			if not isinstance(C, (self.__class__, EmptySet)):
				raise TypeError("TypeError: Collection._bilateral_intersection(x): incorrect type of x")
			
			# check if c is empty set
			if type(C) == EmptySet:
				return EmptySet()

			# check common type
			common_type_name = [typ.__name__ for typ in self.type_limit if (typ.__name__ in self._clusters.keys()) and (typ.__name__ in C.clusters.keys())]

			# prepare a list for intersection 
			common_members = []
			# pick out common members for each type
			for type_name in common_type_name:
				for item in self._clusters[type_name]:
					for item_c in C.clusters[type_name]:
						if type(item) in self.type_limit[-2:]:
							if item.isIdentityOf(item_c):
								common_members.append(item)
								break
						else:
							if item == item_c:
								common_members.append(item)
								break

			# return an intersection
			if common_members == []:
				inter_set = EmptySet()
			else:
				inter_set = Collection(common_members)
			return inter_set

		except Exception as err:
			print(err)

	# intersection
	def intersectionSet(self, *C):
		# one by one
		try:
			for i, c in enumerate(C):
				if not isinstance(c, (self.__class__, EmptySet)):
					raise TypeError("TypeError: Collection.intersectionSet(x): incorrect type of x")
				if i == 0:
					inter_set = self._bilateral_intersection(c)
					if type(inter_set) == EmptySet:
						return EmptySet()
				else:	
					inter_set = inter_set._bilateral_intersection(c)
					if type(inter_set) == EmptySet:
						return EmptySet()
			
			return inter_set
		except Exception as err:
			print(err)

	# bilateral union
	def _bilateral_union(self, C):
		try:
			if not isinstance(C, (self.__class__, EmptySet)):
				raise TypeError("TypeError: Collection._bilateral_union(x): incorrect type of x")
			
			# check if c is empty set
			if type(C) is EmptySet:
				return self
			else:
				# check union type
				union_cluster_type_name = [typ.__name__ for typ in self.type_limit if (typ.__name__ in self._clusters.keys()) or (typ.__name__ in C.clusters.keys())]
				# prepare an union set
				union_set = Collection()

				for type_name in union_cluster_type_name:
					if type_name in self._clusters.keys() and type_name in C.clusters.keys():
						print(type_name)
						union_set.append_all(self._clusters[type_name]+C.clusters[type_name])
					elif type_name in self._clusters.keys() and (type_name not in C.clusters.keys()):
						print(type_name)
						union_set.append_all(self._clusters[type_name])
					else:
						print(type_name)
						union_set.append_all(C.clusters[type_name])
						
				return union_set
		except Exception as err:
			print(err)

	# union set
	def unionSet(self, *C):
		# one by one
		try:
			for i, c in enumerate(C):
				if not isinstance(c, (self.__class__, EmptySet)):
					raise TypeError("TypeError: Collection.unionSet(x): incorrect type of x")
				if i == 0:
					union_set = self._bilateral_union(c)
				else:
					union_set = union_set._bilateral_union(c)
			
			return union_set
		except Exception as err:
			print(err)


	# subset
	def isSubsetOf(self, C):
		try:
			if not isinstance(C, (self.__class__, EmptySet)):
				raise TypeError("TypeError: Collection.isSubsetOf(x): incorrect type of x")
				
			# intersection
			inter_set = self._bilateral_intersection(C)
			# tricky way
			if type(inter_set) == EmptySet:
				return False
			else:
				if inter_set.number_of_members == self._number_of_members:
					return True
				else:
					return False

		except Exception as err:
			print(err)

	# proper subset
	def isProperSubsetOf(self, C):
		try:
			if not isinstance(C, (self.__class__, EmptySet)):
				raise TypeError("TypeError: Collection.isProperSubsetOf(x): incorrect type of x")
				
			# intersection
			inter_set = self._bilateral_intersection(C)
			# tricky way
			if type(inter_set) == EmptySet:
				return False
			else:
				if inter_set.number_of_members == self._number_of_members and inter_set.number_of_members < C.number_of_members:
					return True
				else:
					return False

		except Exception as err:
			print(err)
		

if __name__ == '__main__':
	e1 = entity.Entity('name1', {'1':1,'2':2,'3':3})
	e2 = entity.Entity('name2', {'1':1,'2':2,'3':3})
	e3 = entity.Entity('name3', {'1':1,'2':2,'3':3})
	e4 = entity.Entity('name4', {'1':1,'2':2,'3':3})
	e5 = entity.Entity('name5', {'1':1,'2':2,'3':3})
	e6 = entity.Entity('name6', {'1':1,'2':2,'3':3})
	e7 = entity.Entity('name7', {'1':1,'2':2,'3':3})
	e8 = entity.Entity('name8', {'1':1,'2':2,'3':3})
	e9 = entity.Entity('name9', {'1':1,'2':2,'3':3})
	e10 = entity.Entity('name10', {'1':1,'2':2,'3':3})

	C0 = Collection([e1, 'hello'])

	C1 = Collection([e1, e2, e3, e3, 'hello'])
	print(C1.number_of_members, C1.members)
	#print(C1.clusters)

	print('---------------------------------------------')
	C2 = Collection([e3, e4, e5, e6, 1.0])
	print(C2.number_of_members, C2.members)
	#print(C2.clusters)
	'''
	print('\n\nintersection---------------------------------------------')
	for item in C1.intersectionSet(C2).members:
		if type(item) in [entity.Entity, point.Point]:
			print(item.name)
		else:
			print(item)
	print(C1.intersectionSet(C2).intersectionSet(C0))

	print('\n\nissubset---------------------------------------------')
	print(C1.isSubsetOf(C2), C0.isSubsetOf(C1), C0.isProperSubsetOf(C1))
	print(EmptySet().isProperSubsetOf(C1))

	print('\n\nispropersubset---------------------------------------------')
	print(C1.isProperSubsetOf(C2))
	'''
	'''
	print('\n\nunion---------------------------------------------')
	for item in C1.unionSet(C2).members:
		if type(item) in [entity.Entity, point.Point]:
			print(item.name)
		else:
			print(item)
	'''
	print('--------------------------------------------')
	#print(C1.unionSet(C2).unionSet(C0).members)
	for item in C1.unionSet(C2).unionSet(C0).members:
		if type(item) in [entity.Entity, point.Point]:
			print(item.name)
		else:
			print(item)
	'''
	print('\n\n-----------------------------------------')
	C1.append('world')
	print(C1.number_of_members, C1.members)
	
	print('\n\n-----------------------------------------')
	C2.append(['a', 'b'])
	print(C2.number_of_members, C2.members)

	print('\n\n-----------------------------------------')
	C2.pop(-1)
	print(C2.number_of_members, C2.members)

	print('\n\n-----------------------------------------')
	C1.remove('hello')
	print(C1.number_of_members, C1.members)
	'''
