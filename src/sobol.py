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
		try:
			r.raise_for_status()
			r = r.json()
			for role in r:
				# get custom-field-values for each role
				custom_fields = requests.request("GET", self.base_url+f"/org/{self.org_id}/custom-field-values?objectId={role['_id']}&objectType=role", headers=self.headers)
				custom_fields.raise_for_status()
				custom_fields = custom_fields.json()
				print("response", custom_fields) # for debugging
				for field in custom_fields:
					# append ['_custom-field-name'] : ['content']['text'] to role's json entry
					role[field['_customFieldName']] = field['content']
			return r
		except requests.exceptions.HTTPError as e:
			raise e