# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:21:19 2017

@author: Debraj Ghose

Stupidly simple program to change a specific line in a text file. 

"""




for folder in range(1,5):
    
    filename = str(folder) + '/' + 'boo.txt'
    print filename
    textfile = open(filename,'r') #using 'w' instead of 'r' will create a new file in place of the old one!
    
    g = textfile.readlines() #read the file and store as a string
    print g
    g[2] = 'a = '+ str(folder*20)+'\n' #change the specific line you want to change. Don't forget to include '\n' at the end!
    print g
    textfile = open(filename,'w') #now create a file with the same name to write into
    textfile.writelines( g ) #write contents of g into your text file
    
    textfile.close() #DON'T FORGET TO CLOSE THE FILE OR NOTHING WILL BE WRITTEN






"""
# with is like your try .. finally block in this case
with open('stats.txt', 'r') as file:
    # read a list of lines into data
    data = file.readlines()

print data
print "Your name: " + data[0]

# now change the 2nd line, note that you have to add a newline
data[1] = 'Mage\n'

# and write everything back
with open('stats.txt', 'w') as file:
    file.writelines( data )
    
"""