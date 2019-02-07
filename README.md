# Write by Error404
# LSB decoder


You can use for test the "testPicture.png", the flag is : CDAISIFIC{a*dÃ§^b/vT,A$}

Test command : 

	python3 principale.py -f testPicture.png -P rvb -s




usage: setup.py [-h] [-f FILE] [-P PATTERN] [-p] [-d DIMENSION] [-t] [-s] [-n]
                [-j JUMP]

Error404

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Define your path file
  -P PATTERN, --pattern PATTERN
                        Make a pattern for your search with 'r','v','b','a'
			
			r = red
                        b = blue 
                        v = green 
                        a = transparancy 

  -s, --switch          Switches all the character pattern for all
                        possibilities with 'r','v','b','a'
			

  -d DIMENSION, --dimension DIMENSION
                        Define the search block in x (ex : 0x100)

  -t, --turn            Turn image in other sense

  
  -s, --switch          Reverse the 8 bit
  
  
  -n, --not             Change bit 1 on 0 and bit 0 on bit one
  

  -j JUMP, --jump JUMP  Jump from pixel to pixel

