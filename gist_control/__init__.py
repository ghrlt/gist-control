import requests
from .errors import *


class Gist:
	def __init__(self, oauth_token: str):
		self.oauth = oauth_token

		if not self.isOAuthTokenValid:
			raise InvalidOAuthToken("The token you passed is invalid (Might be expired).")


	def create(self, description: str, files: list, public: bool=True):
		# files = [{"name": "a", "content": "aa"}, {"name": "b", "content": "bb"}]

		r = self.doApiRequest(
			"gists",
			headers={"accept": "application/vnd.github.v3+json"},
			data={
				"description": description,
				"files": {f['name']:{"content":f['content']} for f in files},
				"public": public 
			},
			method="POST"
		)

		return r

	def update(self, gist_id: str, description: str=None, files: list=None):
		# files = [{"name": "a", "content": "aa"}, {"name": "b", "filename"="c", "content": "cc"}]

		_ = self.get_gist(gist_id)

		json = {}
		if description:
			json['description'] = description
		if files:
			json['files'] = {f['name']: {k:v for (k,v) in f.items() if k != "name"} for f in files}


		r = self.doApiRequest(
			f"gists/{gist_id}",
			headers={"accept": "application/vnd.github.v3+json"},
			data=json,
			method="PATCH"
		)

		return r

	
	def update_file(self, gist_id: str, filename: str, new_name: str=None, new_content: str=None):
		_ = self.get_gist(gist_id)

		file = {"name": filename}
		if new_name:
			file['filename'] = new_name
		if new_content:
			file['content'] = new_content

		r = self.update(
			gist_id=gist_id,
			files=[file]
		)

		return r

	def add_file(self, gist_id: str, filename: str, content: str):
		gist = self.get_gist(gist_id)

		if gist['files'].get(filename):
			raise FileAlreadyExists(f'A file with this name "{filename}" already exists in gist {gist_id}')

		return self.update_file(gist_id=gist_id, filename=filename, new_content=content)

	def delete_file(self, gist_id: str, filename: str):
		gist = self.get_gist(gist_id)

		if gist['files'].get(filename):
			return self.update(gist_id=gist_id, files=[{"name": filename}])

		raise FileDoNotExists(f'No file named "{filename}" found in gist {gist_id}')


	def delete(self, gist_id: str):
		_ = self.get_gist(gist_id)

		path = f"gists/{gist_id}"

		r = self.doApiRequest(
			path,
			headers={"accept": "application/vnd.github.v3+json"},
			method="DELETE",
			res_as_json=False
		)
		return r

	def list(self):
		r = self.doApiRequest("gists", headers={"accept": "application/vnd.github.v3+json"})

		return r

	def get_gist(self, gist_id: str):
		r = self.doApiRequest(f"gists/{gist_id}", res_as_json=False)

		if r.status_code == 200 or r.status_code == 304: # Why 304? :shrug: but response code is shown in doc
			return r.json()

		elif r.status_code == 404:
			raise InvalidGistId(f'Gist "{gist_id}" was not found.')

		elif r.status_code == 403:
			raise InvalidGistId(f'Access to gist "{gist_id}" is forbidden.')



	@property
	def isOAuthTokenValid(self):
		r = self.doApiRequest("/user", res_as_json=False)

		if r.status_code == 200:
			return True
		return False

	def doApiRequest(self, path: str, headers: dict={}, data: dict={}, method: str="GET", res_as_json: bool=True):
		headers = {
			"Authorization": f"token {self.oauth}",
			**headers
		}

		if path[0] == "/":
			path = path[1:]

		url = f"https://api.github.com/{path}"

		r = requests.request(method, url, headers=headers, json=data)

		if res_as_json:
			try:
				return r.json()
			except:
				pass

		return r
