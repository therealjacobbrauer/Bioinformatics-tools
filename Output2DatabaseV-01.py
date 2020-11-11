#!/usr/bin/python
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('Output2DatabaseV-01.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('Output2DatabaseV-01.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is "', inputfile)
   print('Output file is "', outputfile)

   a_file = open(inputfile, "r")
   lines = a_file.readlines()
   a_file.close()

   
   outputfile = open(outputfile, "w")
   lineCounter = 0
   printerSwitch = 0
   for line in lines:
       lineCounter = lineCounter + 1
       if line.startswith('>'):
           printerSwitch = 1
           print("lineCounter is: ", lineCounter)
           print(line)
           outputfile.write(line)
           input("press enter")
       elif (printerSwitch == 1):
           outputfile.write(line)

   outputfile.close()



if __name__ == "__main__":
   main(sys.argv[1:])



