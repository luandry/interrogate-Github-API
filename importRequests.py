import requests 
r = requests.get("https://api.github.com/users/luandry")

print(r.content)