usage: py front-back-generator.py

front-back-generator.py looks at the cards.csv file located in the grandparent directory

the file should contain name,count,filename,back,type

given an arbitrary set of cards, in the order listed, each card will be added along with their corresponding back x amount of times, where the back file is specified in the back column, and x is specified in the count column

the resultant merged pdf is output as front-back.pdf

_pdfs is a folder which contains the resources used, and should be updated by exporting from fronts.afphoto and backs.afphoto whenever changes are made. currently there is nothing that automates this step
