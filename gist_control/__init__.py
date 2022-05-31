import requests


class InvalidOAuthToken(Exception):
	pass

class InvalidGistId(Exception):
	pass


class Gist:
	def __init__(self, oauth_token: str):
		self.oauth = oauth_token

		if not self.isOAuthTokenValid:
			raise InvalidOAuthToken("The token you passed is invalid (Might be expired).")


	def create(self, description: str, name: str, content: str, public: bool=True):
		r = self.doApiRequest(
			"gists",
			headers={"accept": "application/vnd.github.v3+json"},
			post={
				"description": description,
				"files": {
					name: {
						"content": content
					}
				},
				"public": public 
			}
		)

		return r

	def delete(self, gist_id: str):
		path = f"gists/{gist_id}"

		r = self.doApiRequest(
			path,
			headers={"accept": "application/vnd.github.v3+json"},
			delete=True
		)
		if r.status_code == 404:
			raise InvalidGistId(f'Gist "{gist_id}" was not found.')

		return r

	def list(self):
		r = self.doApiRequest("gists", headers={"accept": "application/vnd.github.v3+json"})

		return r


	@property
	def isOAuthTokenValid(self):
		r = requests.get(
			"https://api.github.com/user",
			headers={"Authorization": f"token {self.oauth}"}
		)

		if r.status_code == 200:
			return True
		return False

	def doApiRequest(self, path: str, headers: dict={}, post: dict={}, delete: bool=False):
		headers = {
			"Authorization": f"token {self.oauth}",
			**headers
		}

		if path[0] == "/":
			path = path[1:]

		url = f"https://api.github.com/{path}"

		if post:
			r = requests.post(url, headers=headers, json=post)
		elif delete:
			r = requests.delete(url, headers=headers)
		else:
			r = requests.get(url, headers=headers)


		if r.status_code == 200:
			return r.json()

		return r
