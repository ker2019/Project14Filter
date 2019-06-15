class SerieDomainError(Exception):
	pass

#Bool serie
class BSerie:
	def __init__(self, data: 'list[bool]' = [])-> 'BSerie':
		self.data = []
		for i in  range(0, len(data)):
			self.data.append(data[i])
		self.len = len(data)

	def __len__(self):
		return self.len

	def __eq__(self, other):
		a = []
		if isinstance(other, bool):
			for i in range(0, self.len):
				a.append(self.data[i] == other)
		elif isinstance(other, BSerie):
			for i in range(0, self.len):
				a.append(self.data[i] == other.data[i])
		else:
			raise SerieDomainError("Can't compare BSerie with " + str(type(other)))
		return BSerie(a)

	def __or__(self, other):
		a = []
		if isinstance(other, bool):
			for i in range(0, self.len):
				a.append(self.data[i] or other)
		elif isinstance(other, BSerie):
			for i in range(0, self.len):
				a.append(self.data[i] or other.data[i])
		else:
			raise SerieDomainError("Can't compare BSerie with " + str(type(other)))
		return BSerie(a)

	def __and__(self, other):
		a = []
		if isinstance(other, bool):
			for i in range(0, self.len):
				a.append(self.data[i] and other)
		elif isinstance(other, BSerie):
			for i in range(0, self.len):
				a.append(self.data[i] and other.data[i])
		else:
			raise SerieDomainError("Can't compare BSerie with " + str(type(other)))
		return BSerie(a)

	def __ne__(self, other):
		a = []
		if isinstance(other, bool):
			for i in range(0, self.len):
				a.append(self.data[i] != other)
		elif isinstance(other, BSerie):
			for i in range(0, self.len):
				a.append(self.data[i] != other.data[i])
		else:
			raise SerieDomainError("Can't compare BSerie with " + str(type(other)))
		return BSerie(a)

	def __getitem__(self, key):
		if isinstance(key, int):
			return self.data[key]
		elif isinstance(key, BSerie):
			a = []
			for i in range(0, self.len):
				if key[i]: a.append(self.data[i])
			return BSerie(a)
		else:
			raise SerieDomainError("Can't get items from BSerie by " + str(type(key)))

	def __str__(self):
		return str(self.data)

#Float serie
class Serie:
	def __init__(self, data: 'list[float]' = [])-> 'Serie':
		self.data = []
		for i in  range(0, len(data)):
			self.data.append(data[i])
		self.len = len(data)

	def __len__(self):
		return self.len

	def __eq__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] == other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] == other.data[i])
		else:
			raise SerieDomainError("Can't compare Serie with " + str(type(other)))
		return BSerie(a)

	def __lt__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] < other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] < other.data[i])
		else:
			raise SerieDomainError("Can't compare Serie with " + str(type(other)))
		return BSerie(a)

	def __le__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] <= other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] <= other.data[i])
		else:
			raise SerieDomainError("Can't compare Serie with " + str(type(other)))
		return BSerie(a)

	def __gt__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] > other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] > other.data[i])
		else:
			raise SerieDomainError("Can't compare Serie with " + str(type(other)))
		return BSerie(a)

	def __ge__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] >= other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] >= other.data[i])
		else:
			raise SerieDomainError("Can't compare Serie with " + str(type(other)))
		return BSerie(a)

	def __ne__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] != other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] != other.data[i])
		else:
			raise SerieDomainError("Can't compare Serie with " + str(type(other)))
		return BSerie(a)

	def __getitem__(self, key):
		if isinstance(key, int):
			return self.data[key]
		elif isinstance(key, BSerie):
			a = []
			for i in range(0, self.len):
				if key[i]: a.append(self.data[i])
			return Serie(a)
		else:
			raise SerieDomainError("Can't get items from Serie by " + str(type(key)))

	def __str__(self):
		return str(self.data)

	def __add__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] + other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] + other.data[i])
		else:
			raise SerieDomainError("Can't add " + str(type(other)) + " to Serie")
		return Serie(a)

	def __sub__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] - other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] - other.data[i])
		else:
			raise SerieDomainError("Can't sub " + str(type(other)) + " to Serie")
		return Serie(a)

	def __mul__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(self.data[i] * other)
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(self.data[i] * other.data[i])
		else:
			raise SerieDomainError("Can't mul " + str(type(other)) + " to Serie")
		return Serie(a)

	def __radd__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(other + self.data[i])
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(other.data[i] + self.data[i])
		else:
			raise SerieDomainError("Can't add Serie to " + str(type(other)))
		return Serie(a)

	def __rsub__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(other - self.data[i])
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(other.data[i] - self.data[i])
		else:
			raise SerieDomainError("Can't sub Serie to " + str(type(other)))
		return Serie(a)

	def __radd__(self, other):
		a = []
		if isinstance(other, float) or isinstance(other, int):
			for i in range(0, self.len):
				a.append(other * self.data[i])
		elif isinstance(other, Serie):
			for i in range(0, self.len):
				a.append(other.data[i] * self.data[i])
		else:
			raise SerieDomainError("Can't mul Serie to " + str(type(other)))
		return Serie(a)


MySer = Serie([1, 2, 3, 4, 5, 6, 7, 19, -34, 6.7])
print(MySer[MySer * 2 + 1 <= 5])
