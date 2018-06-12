from unittest import TestCase
import part01 as p01


class TestKnock01(TestCase):
	def test_knock00(self):
		expected = "desserts"
		actual = p01.knock00()
		self.assertEquals(expected, actual)
	
	def test_knock01(self):
		expected = "パトカー"
		actual = p01.knock01()
		self.assertEquals(expected, actual)
		
	def test_knock02(self):
		expected = "パタトクカシーー"
		actual = p01.knock02()
		self.assertEquals(expected, actual)
		
	def test_knock03(self):
		expected = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9]
		actual = p01.knock03()
		self.assertEquals(expected, actual)

	def test_knock04(self):
		expected = {'H': 1, 'He': 2, 'Li': 3, 'Be': 4, 'B': 5, 'C': 6, 'N': 7, 'O': 8, 'F': 9, 'Ne': 10, 'Na': 11, 'Mi': 12, 'Al': 13, 'Si': 14, 'P': 15, 'S': 16, 'Cl': 17, 'Ar': 18, 'K': 19, 'Ca': 20}
		actual = p01.knock04()
		self.assertEquals(expected, actual)
