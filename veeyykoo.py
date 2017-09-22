# -*- coding: utf-8 -*-
"""
Created on Sat May 13 18:00:44 2017

@author: extvylik
"""
import re
from sys import argv

fixed_data = []
script, inputfile, outputfile = argv

#Check that input file can be opened and read, If not throw an exception.
try:
    f = open(inputfile, "r")
    print "File read successfully!!"
    # Fetch data from input file
    raw_data = f.readlines()
    # closing file when done
    f.close()
except IOError:
    print "Error: File " + inputfile + " does not appear to exist!!!" 


#Parse rows which contains exactly three integers.
for line in raw_data:
    count_of_int = (re.findall('\d+', str(line))) 
    if (len(count_of_int) == 3):
        fixed_data.append(line)


'''This method creates multiplies of X and Y. It takes fixeddata as an input and
will return list which contains goal value and all multiplies values.'''
def create_multiplies(data):
    allrows = []
    for j in range(0, len(data)):
        #Parsing only numbers from row.
        numbers = (re.findall('\d+', str(data[j])))
        row = []
        for i in range(1,int(numbers[2])):
            if (i % int(numbers[0]) == 0) or (i % int(numbers[1]) == 0):
                row.append(i)
        #Adding goal value to list too        
        row.append(numbers[2])
        #Gather all rows together
        allrows.append(row)
    return(allrows)
  
  
'''This method will sort data and print it to screen in form where first number
is goal number and then all multiplies of X and Y in ascending order. It 
takes multiplies list as an input and returns output string which will be 
saved to output file'''
def sort_data(data):
    sorted_data = sorted(data, key = lambda x: int(x[-1]), reverse = True)
    output = ""
    for i in range(0, len(sorted_data)):
        output += str(sorted_data[i][-1]) + ": " + str(sorted_data[i][0:-1]) + "\n"
    return output

#Print formatted data to screen
multiplies = create_multiplies(fixed_data)
print (sort_data(multiplies))    

#Save formatted data to output file
f2 = open(outputfile, "w+")
f2.write(str(sort_data(multiplies)))
f2.close()