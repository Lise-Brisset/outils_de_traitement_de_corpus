import requests
import lxml.html

url = 'https://fr.wikipedia.org/wiki/Chat'
r = requests.get(url)
#r.status_code
#print(r.content)

root = lxml.html.fromstring(r.content)

## exemple pour mieux comprendre la manipulation d'objet xml :
#toutledoc = root.xpath("/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/p[4]/a[7]")
#print("=============ELEMENT===============")
#print(toutledoc[0])
#print("==========CONTENU TEXTUEL===========")
#print(toutledoc[0].text_content())
#print("=============HREF==================")
#print(toutledoc[0].attrib['href'])


introduction = root.xpath("//div[@id='bodyContent']//p|//div[@id='bodyContent']//h2")
# print(introduction)

def get_urls():
    """ vient récupèrer tous les liens présents sur la page de départ """
    dico_urls = {}
    id=1
    for p in introduction:
        try:
            a_tag = p.xpath('.//a')[0]
            href = a_tag.attrib['href']
            # on vérifie que c'est un lien wikipédia
            if href.startswith('/wiki/'):
                # dans le cas de notre page, tous les href sont des chemins relatifs
                dico_urls[id] = ('https://fr.wikipedia.org' + href, a_tag.text_content().replace(" ","_"))
            else:
                pass
            id+=1
        # dans le cas où le p est vide et ne contient donc pas de balise a
        except IndexError:
            pass

    return dico_urls

urls = get_urls()


def get_first_header_text(root):
    """ récupère le contenu textuel de l'introduction de la page visitée """
    intro = root.xpath("//div[@id='bodyContent']//p|//div[@id='bodyContent']//h2") # on récupère les éléments qui nous intéressent

    text = []

    for paragraph in intro:
        if paragraph.tag != "h2":
            text.append(" ".join(paragraph.xpath(".//text()")))
        else:
            return " ".join(text).replace("\n", "")

# pour afficher le contenu de l'intro de la première page
#print(get_first_header_text(root))

def save_txt(text_content, file_name):
    """ enregistre sous format txt le contenu textuel de la page visitée """
    with open(f"../../data/clean/{file_name}", "w") as fichier:
        fichier.write(text_content)


def save_all_urls_contents(urls_dico):
    """ Permet de parcourir toutes nos urls et d'enregistrer automatiquement les contenus de chacune de ces pages dans des fichiers textes."""
    compte = 0
    for url in urls_dico.values():
        # condition d'arrêt de la boucle ajoutée pour ne pas récupérer plus de 50 pages, plus n'étant pas spécialement utile dans ce projet
        if compte <= 50:
            req = requests.get(url[0])
            the_root = lxml.html.fromstring(req.content)
            # on récupère le contenu de l'url sur laquelle nous sommes
            content = get_first_header_text(the_root)
            # on peut rencontrer des contenus vides (page pas non remplie comme celle de https://fr.wikipedia.org/wiki/Mathou
            if content is not None:
                # on enregistre sous format txt le contenu de l'url
                save_txt(content, f"{url[1]}.txt")
                compte += 1
            else:
                pass
    print("Scrapping terminé !")


save_all_urls_contents(urls)

