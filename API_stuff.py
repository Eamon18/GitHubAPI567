import requests
import json

def get_user_info(id):
	user = requests.get('https://api.github.com/users/{}/repos'.format(id))
	user_data =json.loads(user.text)

	repo_list = []
	user_dict = {}

	for repo in user_data:
		repo_name = repo['name']

		commits = requests.get('https://api.github.com/repos/{}/{}/commits'.format(id,repo_name))
		commits_data = json.loads(commits.text)	#returns json of commits info

		user_dict[repo_name] = len(commits_data)

	for key in user_dict:
		print(key + ": " + str(user_dict[key]))

	return user_dict




get_user_info("Eamon18")