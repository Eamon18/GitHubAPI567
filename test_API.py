import unittest

from API_stuff import get_user_info
from unittest.mock import Mock, patch


class TestAPI(unittest.TestCase):

	@patch('API_stuff.get_user_info')
	def test_mock_get_user_info(self, mock_info):
		repos = {'AVEDS': 20,
			'GitHubAPI567': 4,
			'SSW567-HW02ello-world': 3,
			'SpotifyMe': 6,
			'SSW-555-A_Group_Project': 1,
			'SSW-567': 1,
			'SSW567-HW02': 4,
			'SSW567-Static-Analysis': 2}

		mock_info.return_value = repos

		response = get_user_info('Eamon18')

		assertDictContainsSubset(repos,response)



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
