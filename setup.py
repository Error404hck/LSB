'''
    Main program 
    
    Write by : 
             _____                     _  _    ___  _  _   
            | ____|_ __ _ __ ___  _ __| || |  / _ \| || |  
            |  _| | '__| '__/ _ \| '__| || |_| | | | || |_ 
            | |___| |  | | | (_) | |  |__   _| |_| |__   _|
            |_____|_|  |_|  \___/|_|     |_|  \___/   |_|  
                                             
    
    Descrition: This code allows to find hidden data in lsb files
                    This file allows you to select an image and play the variables of convertLsb.py
                    with all possible possibilities.


            setup.py
            lsbFunction/
             |_________: __init__.py
             |_________: convertLsb.py
            ascciDir/
             |_________: *.txt     
                   
''' 

# Import library and function : 
from lsbFunction import convertLsb as clsb
from PIL import Image
import itertools
import argparse
##############################################


# Argument parser :
parser = argparse.ArgumentParser(description="Error404")
parser.add_argument('-f', '--file', type=str, default="", help="Define your path file") #--> select picture
parser.add_argument('-P', '--pattern', type=str, default="", help="Make a pattern for your search with 'r','v','b','a'") #--> choose pattern
parser.add_argument('-p', '--possibilities', action='store_true' , default=False, help="Test all the character pattern for all possibilities with 'r','v','b','a'") #--> activate switch possibilities
parser.add_argument('-d', '--dimension', type=str, default=False, help="Define the search block in x (ex : 0x100)") #--> choose the research dimension
parser.add_argument('-t', '--turn', action='store_true', default=False, help="Turn image in other sense") #--> turn image in other sense
parser.add_argument('-s', '--switch', action='store_true', default=False, help="Reverse the 8 bit") #--> reverse the bit
parser.add_argument('-n', '--not', action='store_true', default=False, help="Change bit 1 on 0 and bit 0 on bit one") #--> reverse the bit
parser.add_argument('-j', '--jump', type=str, default=1, help="Jump from pixel to pixel") #--> jump from pixel to piexel
dargs = vars(parser.parse_args())
##############################################


# Variable :
fileName = dargs['file']
pattern  = dargs['pattern']
possibilitiesSys = dargs['possibilities']
turnImage = dargs['turn']
switchBit = dargs['switch']
notBit = dargs['not']
jump = dargs['jump']
try :
    searchBlockX = int(dargs['dimension'].split("x")[0])
    searchBlockY = int(dargs['dimension'].split("x")[1])
except :
    searchBlockX = False
    searchBlockY = False
###############################################

# Select Image :
try :
    pic = Image.open(fileName)
except :
    print("Bad path ..." + "\"" + fileName + "\"" + " Not Found.")
    exit()
###############################################


# Main function :
def stego (pic,pattern) :
    
    # Make all switche possibilities with pattern
    if possibilitiesSys == True :
        for i in range (1,len(pattern)+1):
            a = (list(itertools.permutations(pattern,i)))

            for j in range (0,len(a)):
                typePixel = "".join(a[j])
                if searchBlockX == False and searchBlockY == False:
                    clsb.writeFile(typePixel, pic, jump, turnImage, switchBit, notBit)
                else :
                    clsb.writeFile(typePixel, pic, jump, turnImage, switchBit, notBit, searchBlockX, searchBlockY , searchBlockX , searchBlockY)

    # Make just one possibilities with the pattern
    elif possibilitiesSys == False :
        if searchBlockX == False and searchBlockY == False:
            clsb.writeFile(pattern,pic, jump, turnImage, switchBit, notBit)
        else : 
            clsb.writeFile(pattern, pic, jump, turnImage, switchBit, notBit, searchBlockX, searchBlockY, searchBlockX, searchBlockY)

# Play the script :
if __name__ == "__main__" : 
    stego(pic,pattern)
