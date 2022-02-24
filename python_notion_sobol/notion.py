import os
import requests
from requests.structures import CaseInsensitiveDict

class Notion(object):
	def __init__(self):
		super(Notion, self).__init__()
		self.base_url = "https://api.notion.com"
		self.api_key = os.environ.get('notion_api_key')
		self.database_id = os.environ.get('notion_db_id')
		self.headers = CaseInsensitiveDict()
		self.headers["Accept"] = "application/json"
		self.headers["Content-Type"] = "application/json"
		self.headers["Authorization"] = f"Bearer {self.api_key}"
		self.headers["Notion-Version"] = "2021-08-16"

	def write_row(self, data):
		r = requests.request("POST", self.base_url+'/v1/pages/', headers=self.headers, data=data)
		# print(r.status_code, "anthing 200-299 is good. anything else is bad.")	# for Debugging
		r = r.json()
		return r