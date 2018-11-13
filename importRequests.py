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

# Data to plot
labels = 'Vain(Followers)', 'Humble(Following)'
sizes = [followers, following]
colors = ['gold', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=140)
 
plt.axis('equal')
plt.title('Vanity Checker, checks Followers vs Following')
plt.show()










#print('Followers: ' ,followers)
#print('following: ', following)



#print('Received Data: ', json.dumps(data, sort_keys = True, indent = 4))

#print(r.text)

#want to take in a username, 
#find all their number of repos, 
#and number of total commits, 
#and compare them with some sort of graph
#maybe compare number of followers with number of people following