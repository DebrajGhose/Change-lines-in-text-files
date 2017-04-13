# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:21:19 2017

@author: Debraj Ghose

Stupidly simple program to change a specific line in a text file. 

"""
from glob import glob


#paths = glob('*/') #get all files in current directory

#paths = [p[:-1] for p in paths] #strip off trailing backslashes

#for folder in paths: 

for folder in range(1,5):
    
    filename = str(folder) + '/' + 'boo.txt'
    
    textfile = open(filename,'r') #using 'w' instead of 'r' will create a new file in place of the old one!
    
    g = textfile.readlines() #read the file and store as a string
    
    g[2] = 'a = '+ str(folder*20)+'\n' #change the specific line you want to change. Don't forget to include '\n' at the end!
    
    textfile = open(filename,'w') #now create a file with the same name to write into
    textfile.writelines( g ) #write contents of g into your text file
    
    textfile.close() #DON'T FORGET TO CLOSE THE FILE OR NOTHING WILL BE WRITTEN



