#!/bin/python3
from wikipedia import *

i = input('Choose language>')
set_lang(i)

cycle = True

print ('WikiSeach\nVer 0.0.2')

while cycle == True:
    i = input('seach>')
    
    if i == "/exit":
        cycle = False
        
    else:
        page = wikipedia.page(i)
        print (page.title)
        print ('Url -', page.url)
        con = page.content
        print(page.content)
        
        c = input('Save article?(y/n)')
        if c == 'y':
            path = input('Enter path to file>')
            file = open(path, "w")
            file.write(con)
            file.close
        else: pass
