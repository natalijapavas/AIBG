## Requests
`sudo apt install python3-requests`

```python
import requests

URL = 'https://....'
AUTH = ('uname', 'passwd')
HEADERS = {} # key value pairs

params = {} # key value pairs
# Get 
r = requests.get(URL, AUTH, params=params, headers=headers)

if r.status_code != requests.codes.ok:
	print("[-] Error, request for {} failed".format(r.url))
	exit(-1)

r.text 
r.json()
```

## Flask
`sudo apt install python3-flask`

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
	return "Yet Another Coding Crew"

@app.route('/action', methods=['GET', 'POST'])
def action(req):
	if request.method == 'POST':
		# parse post request
	elif request.method == 'GET':
		parse get request
	else:
		return "something is wrong"



if __name__ == '__main__':
	app.run()
```
