import requests
from bs4 import BeautifulSoup
from urllib.parse import quote, unquote
import os

bibUrl = "https://the-eye.eu/public/Books/Bibliotik/"
indexPath = "./index.txt"

def create_index():
    # 1 GET DIRECTORY URLS
    bibSoup = BeautifulSoup(requests.get(bibUrl).content , 'html.parser')
    letterUrls = [bibUrl + a.get_text() for a in bibSoup.find_all('a',text=lambda x: '/' in x)[1:]]

    # 2 GET BOOK NAMES
    lenBibUrl = len(bibUrl)
    soupList = [BeautifulSoup(requests.get(x).content, 'html.parser') for x in letterUrls]
    hrefs = [letterUrls[i][lenBibUrl:] + unquote(a['href']) + '\n' for i, soup in enumerate(soupList) for a in soup.find_all('a', href=lambda x:"https" not in x and x != "../")]

    # 3 WRITE NAMES TO FILE
    try:
        with open(indexPath, 'x') as f:
            f.writelines(hrefs)
    except FileExistsError:
        print("Index file already exists")


def get_link(name):
    return bibUrl+name

def main():
    titleList = []
    try:
        with open(indexPath, 'r') as f:
            titleList = f.read().splitlines()
            
    except FileNotFoundError:
        print("Index file doesn't exist... Creating one")
        create_index()
    input("\nPress any key to continue")
    os.system('clear')

    while True:
        terms = input("Welcome to Bibliotik!\nSearch for: ").lower().rsplit(' ')
        
        matches = [title for title in titleList if all(term in title.lower() for term in terms)]
        
        for i, match in enumerate(matches):
            print("%d %s" % (i, os.path.basename(match)))
        
        s = input("\nEnter file #(s) to download: ")
        
        if s is 'a':
            for match in matches:
                cmd = 'wget -q --show-progress "' + bibUrl + match + '"'
                os.system(cmd)
        else:
            sList = s.rsplit()
            for x in sList:
                ID = -1

                try:
                    ID = int(x)
                    if ID < 0 and ID >= len(matches):
                        raise ValueError('jejox')
                except ValueError:
                    print("Not a valid int!")
                else:
                    cmd = 'wget -q --show-progress "' + bibUrl + matches[ID] + '"'
                    os.system(cmd)
        
        print("\nDone!")        
        input("\nPress ENTER to continue")
        os.system('clear')

if __name__ == '__main__':
    main()
