import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

data = requests.get(url="https://opentdb.com/api.php", params=parameters)
data.raise_for_status()
data = data.json()

question_data = data["results"]
