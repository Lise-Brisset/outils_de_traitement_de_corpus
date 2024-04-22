""" https://www.geeksforgeeks.org/python-requests-tutorial/ """

import requests 
   
# Making a GET request 
r = requests.get('https://fr.wikipedia.org/wiki/Chinchilla') 
  
# check status code for response received 
# success code - 200 
print(r) 
  
# print content of request 
print(r.content) 