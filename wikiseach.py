from wikipedia import *

i = input('Choose language(ru/eng/fr)>')
if i == "ru":
    set_lang('ru')
elif i == "eng":
    set_lang('eng')
elif i == "fr":
    set_lang('fr')
else:
    print ("English selected")

cycle = True

print ('WikiSeach by teamur\nVer 0.0.1')

while cycle == True:
    i = input('seach>')
    
    if i == "/exit":
        cycle = False
        
    else:
        page = wikipedia.page(i)
        print (page.title)
        print ('Url -', page.url)
        print(page.content)