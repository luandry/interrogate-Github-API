import requests 
import json 
import sys
import matplotlib.pyplot as plt, mpld3

userName = sys.argv[1]

#print(userName)

r = requests.get("https://api.github.com/users/" + userName)

data = r.json()

followers = data["followers"]
following = data["following"]

follow = followers, following

print(follow)
#print (1)
#sys.styout.flush()

## Data to plot
labels = 'Vain(Followers)', 'Humble(Following)'
sizes = [followers, following]
colors = ['gold', 'lightskyblue']

plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=140)
 
plt.axis('equal')
plt.title('Vanity Checker, checks Followers vs Following')

mpld3.show()

#mpld3.show()
#lol = mpld3.fig_to_html(plt, d3_url=None, mpld3_url=None, no_extras=False, template_type='general', figid=None, use_http=False)
#print(lol)


#fit_to_html(plt)show()
#plt.show()


