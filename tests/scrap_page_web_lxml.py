
import requests

r = requests.get('https://fr.wikipedia.org/wiki/Chinchilla')
#r.status_code

#print(r.content)



import lxml.html

root = lxml.html.fromstring(r.content)
root.xpath("//div[@id='bodyContent']//p/text()")

def get_first_header_text(root):
    text = []
    for paragraph in root.xpath("//div[@id='bodyContent']//p|//div[@id='bodyContent']//h2"):
        
        if paragraph.tag != "h2":
            text.append(" ".join(paragraph.xpath(".//text()")))
        else:
            return " ".join(text).replace("\n", "")

print(get_first_header_text(root))

# r = requests.get('https://en.wikipedia.org/wiki/Information_theory')
# it_root = lxml.html.fromstring(r.content)
# get_first_header_text(it_root)

