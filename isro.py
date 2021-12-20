import json
import requests


API = "https://isro.vercel.app/api/"


def spacecrafts():
    api = API + "spacecrafts"
    response = requests.get(api).json()
    data = json.dumps(response, indent=4)
    return data


def launchers():
    api = API + "launchers"
    response = requests.get(api).json()
    data = json.dumps(response, indent=4)
    return data


def customer_satellites():
    api = API + "customer_satellites"
    response = requests.get(api).json()
    data = json.dumps(response, indent=4)
    return data


def centres():
    api = API + "centres"
    response = requests.get(api).json()
    data = json.dumps(response, indent=4)
    return data
