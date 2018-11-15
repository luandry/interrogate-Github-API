import requests 
import json 
import sys
import matplotlib.pyplot as plt

userName = sys.argv[1]

#print(userName)

r = requests.get("https://api.github.com/users/" + userName)

data = r.json()

followers = data["followers"]
following = data["following"]

print(followers)
print(following)
sys.styout.flush()

## Data to plot
#labels = 'Vain(Followers)', 'Humble(Following)'
#sizes = [followers, following]
#colors = ['gold', 'lightskyblue']

#plt.pie(sizes, labels=labels, colors=colors,
#        autopct='%1.1f%%', startangle=140)
 
#plt.axis('equal')
#plt.title('Vanity Checker, checks Followers vs Following')
#plt.show()


