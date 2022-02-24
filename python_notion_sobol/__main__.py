import json
import time
from python_notion_sobol.notion import Notion
from python_notion_sobol.sobol import Sobol

# Read from Sobol
my_sobol = Sobol()
my_notion = Notion()

sobol_response = my_sobol.read_roles()
# print(sobol_response)
for i in sobol_response:
	# print(i['name']) # For debugging
	# Write to Notion

	data = {
		"parent": { "database_id": my_notion.database_id}, # set in environment var
	    "properties": {
	        "Name": {
				"title":[ { "text" : { "content" : i['name'] } } ]
			},
			"Status": {
				"select": {
					"name": i['status'],
					"color": "default"
				}
			},
			"Assignees": {
				"rich_text": [{
					"text": { "content" : "FirstName LastName"}
				}]
			},
			"Team": {
				"rich_text": [{
					"text": { "content" : "TeamName"}
				}]	
			},
			"Purpose": {
				"rich_text": [{
					"text": { "content" : "PurposeHere"}
				}]
			},
			"Accountabilities": {
				"rich_text": [{
					"text": { "content" : "AccountabilitiesHere"}
				}]
			},
			"Allocation": {
				"number": i['userAllocationPercent']
			},
			"Projects": {
				"rich_text": [{
					"text": { "content" : "This person has that project"}
				}]
			},
			"Domains": {
				"rich_text": [{
					"text": { "content" : "DescribeDomainHere"}
				}]
			}
	    }	# Payload of sobol data being sent to notion
	}

	data = json.dumps(data) # json formatting

	notion_response = my_notion.write_row(data) # writing payload to notion db
	time.sleep(5) # to avoid too many requests
quit()