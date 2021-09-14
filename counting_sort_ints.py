# Implementation of counting (key-index) sorting

# Given a list of integers
# Assume a radix of the elements of the integer set

def count_sort(array : list[int], radix : int = 10) -> list[int]:
	if not array:
		return None
		
	size = len(array)
	
	if size == 1:
		return array

	# create the count and auxiliary arrays
	count = [0] * (radix + 1)
	aux_array = [0] * size

	# get the frequency of the elements in the original array
	for i in range(size):
		count[array[i] + 1] += 1
	
	# compute the cumulative frequency of the elements in the array
	for r in range(radix):
		count[r + 1] += count[r]

	# extract the array in the correct positions in the auxiliary array
	for i in range(size):
		pos = count[array[i]]
		aux_array[pos] = array[i]
		pos += 1
	
	return aux_array
	
	
import unittest

class TestCountSort(unittest.TestCase):
	def setUp(self):
		self.array_none = None
		self.array_one  = [3]
		self.array_ok   = [9,1,3,2]
		
	def test_array_none(self):
		self.assertEqual(None, count_sort(self.array_none))
		
	def test_array_one(self):
		self.assertEqual([3], count_sort(self.array_one))
		
	def test_array_ok(self):
		self.assertEqual([1,2,3,9], count_sort(self.array_ok))
		

if __name__ == "__main__":
	unittest.main()
		

