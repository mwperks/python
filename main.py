myFile=open ("DataFile.txt", "r") #tells python read only
fileText=myFile.read() #reads the whole file
# fileText=myFile.readline() #reads current line only
print(fileText) #prints out the details

myFile.close()
