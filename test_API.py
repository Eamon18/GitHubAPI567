import unittest

from API_stuff import get_user_info


class TestAPI(unittest.TestCase):

	def test_API_stuff(self):
		correct_info = get_user_info('Eamon18')
		incorrect_info = get_user_info("Eamon")
		self.assertEqual(correct_info['SpotifyMe'],6)
		self.assertEqual(correct_info['AVEDS'],20)
		self.assertEqual(correct_info['hello-world'],3)




if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()