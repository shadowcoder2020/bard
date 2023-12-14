import requests
import anticens

anticens.enable()

res = requests.get("https://bard.google.com")
print(res)