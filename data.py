import requests

URL_API = "https://opentdb.com/api.php"
PARAMETERS = {
        "amount": 10,
        "type": "boolean",
        }

response = requests.get(url=URL_API,
                        params=PARAMETERS)
response.raise_for_status()
question_data = response.json()["results"]
