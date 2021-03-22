import requests
from bs4 import BeautifulSoup
from sys import argv

def realurl(url):
    if "http://" in url or "https://" in url:
        return True
    else:
        return False

def containsslash(url):
    if url[-1] != "/":
        url = url + "/"
    if url[0] == "/":
        url = url[1:]

    return url

def walkthrough(original):
    original = containsslash(original)
    #test original url for slashes
    
    nextlinks = []
    #create empty list for child links

    soup = BeautifulSoup(r.text, features ="html.parser")
    
    r=requests.get(original)

    for a in soup.find_all("a", href=True):
        nextlink = containsslash(a["href"])
        if realurl(nextlink) == False:
            nextlink = original + nextlink
        nextlinks.append(nextlink)
        #after running test add link to list

    return nextlinks

def testurl(urldepth, url):
    try:
        r = requests.get(url)
        if r.status_code not in [200, 302]:
            print(url, "IS A BAD LINK")
            return
            #if status code is not 200 or 302 it is considered bad link
    except:
        print(url, "IS A BAD LINK")
        return
            #return bad link if no status code is returned
        if urldepth > 0:
            nextlinks = walkthrough(url)
            for link in nextlinks:
                testurl(urldpeth-1, link)
                #Run the tests on the child links of the user enters a depth


if __name__ == "__main__":
    if len(argv) == 2:
        url = argv[1]
        testurl(0, url)
        #test if user does not enter a depth
    elif len(argv) ==3:
        urldepth = argv[1]
        url = argv[2]
        if urldepth.startswith("-"):
            try:
                urldepth = int(urldepth[1:])
                #If url depth is entered use value after '-' as depth
            except:
                print("ERROR WITH DEPTH TRY AGAIN")
                exit(1)
                #if error is entered tell user and exit program
            testurl(urldepth, url)
        else:
            print("ERROR ENTER AS FOLLOWING: find-dead-links <URL>")
            print("ERROR ENTER AS FOLLOWING: -<depth> <URL>")
            #Return error message if user does not enter things correctly. 






