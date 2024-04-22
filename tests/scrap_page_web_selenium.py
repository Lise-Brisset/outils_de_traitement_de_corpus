""" https://openclassrooms.com/forum/sujet/recuperer-le-contenu-dune-page-web-en-python """

from selenium import webdriver
 
driver = webdriver.Firefox()
 
driver.get("https://fr.wikipedia.org/wiki/Chinchilla")
 
e=driver.find_element_by_id("bodyContent").text
 
print(e)
 
driver.close()