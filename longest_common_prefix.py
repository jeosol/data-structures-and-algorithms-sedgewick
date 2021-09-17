from typing import Optional

def longest_common_prefix(str1 : str, str2 : str) -> str:
	"""Return the longest_common_prefix between two strings str1 and str2."""
	
	# Check that both arguments are of type string, otherwise return
	if type(str1) != str or type(str2) != str:
		return None
		
	# Get the length of the shortest string
	min_len = min(len(str1), len(str2))
	
	end_index = 0	
	# move through both strings, if we get a match, increment pointer otherwise break
	# out of the loop 
	
	while (end_index < min_len):
		if str1[end_index] == str2[end_index]:
			end_index += 1
		else:
			break
	
	# return the string in the interval [0, end_index)
	return str1[0:end_index]
	
# Test code	
import unittest

class TestLCP(unittest.TestCase):
	def setUp(self):
		self.str1 = 'americano'
		self.str2 = 'americanize'
		
	def test_lcp_wrong_type(self):
		self.assertEqual(None, longest_common_prefix(10, 10))
	
	def test_lcp_correct(self):
		self.assertEqual('american', longest_common_prefix(self.str1, self.str2))
		
if __name__ == "__main__":
	unittest.main()
	
