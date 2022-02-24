import os
import requests
from requests.structures import CaseInsensitiveDict

class Sobol(object):
	def __init__(self):
		super(Sobol, self).__init__()
		self.base_url = "https://sobol.io/d/api/v1"
		self.api_key = os.environ.get('sobol_api_key')
		self.org_id = "gitcoin"
		self.headers = CaseInsensitiveDict()
		self.headers["Accept"] = "application/json"
		self.headers["Authorization"] = f"Bearer {self.api_key}"

	def read_roles(self):
		r = requests.request("GET", self.base_url+f"/org/{self.org_id}/roles", headers=self.headers)
		# print(r.status_code, "anthing 200-299 is good. anything else is bad.")	# for Debugging
		r = r.json()
		return r