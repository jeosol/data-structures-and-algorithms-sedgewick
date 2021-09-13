import math

class Alphabet:
	def __init__(string : str) -> None:
		self.alphabet = string
		self.radix = len(string)
		self.indices = { k : v for (k, v) in zip(string, range(self.radix)}
		
	def radix(self):
		"""Return the number of characters in the alphabet."""
		return self.radix
	
	def logR(self):
		"""Number of bits to represent an index."""
		if self.radix > 0:
			return math.log(self.radix, 2)		
		
	def toChar(self, index : int) -> str:
		"""Convert index to corresponding alphabet char."""
		if index >= 0 and < self.radix:
			return self.alphabet[index]
				
	def toIndex(self, char : str) -> int:
		"""Convert char to an index between 0 and R-1."""
		if char in self.indices:
			return self.indices[char]
		return None
				
	def toIndices(self, string : str) -> list:
		"""Convert string to base-R integer."""
		if string:
			return [self.toIndex(string[i]) for i in range(len(string))]
		
	def toChars(self, indices : list) -> str:
		"""Convert base-R integer to string over this alphabet."""
		if indices:
			return [self.toChar(indices[i]) for i in range(len(indices))]
			

		
		
