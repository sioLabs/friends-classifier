import re

from bs4 import BeautifulSoup
from urllib import urlopen



def linkImporter(baseURL):
    scripts=[]
    html = urlopen(baseURL).read()
    raw = BeautifulSoup(html)
    links = raw.find_all("a")

    for link in links:
        s = link.string.extract()
        print(s)
        # print(link.find('season'))
        if link.find('Episode') > 0:
            print link
            scripts.append(link)

    return scripts


list1= ['phoebe', 'joey', 'chandler', 'rachel', 'monica', 'ross']

def parseline(line):
    #remove everything in parenthesis and square brackets
    line = re.sub("[\(\[].*?[\)\]]", "", line)
    line = line.strip()



    #first find the index of the :
    ind = line.find(":")
    speaker=""
    dialogue=""
    if ind>0:
        #dialogue found. now get the speaker
        speaker = line[:ind]
        try:
            ex = list1.index(speaker)
        except ValueError:
            speaker=""
            return speaker,dialogue

        #find the dailogue
        dialogue = line[ind+2:]
        dialogue = re.sub('[^A-Za-z0-9 ]+', '', dialogue)

    return speaker,dialogue




url = "http://www.livesinabox.com/friends/scripts.shtml"
scripts = linkImporter(url)
print(scripts)

html = urlopen(url).read()
raw = BeautifulSoup(html)
raw = raw.get_text();
indx = raw.find("]")+1;
raw = raw[indx:]
raw = raw.encode('ascii','ignore').lower()

f = open('e01.txt', 'w')



fields = raw.split("\n")

clean =[]
#if there is no : char in the line then append it to last one
for i in range(len(fields)):

    line = fields[i]
    # print(i),(" " +line  )
    if line.find(":") < 0 :

        try:
            str = clean.pop()
            clean.insert(i, str +" "+ line)

             # clean.pop(i+1)
        except IndexError:
             continue

    else :
        clean.insert(i, line)



# print(clean)

for i in range(len(clean)):

    line = clean[i]

    # print(line)
    sp, di = parseline(line)
    if(len(sp)>0):
        print(sp +'(:)'+ di)
        # print()




#print(raw.get_text())
