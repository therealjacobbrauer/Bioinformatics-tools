#!/usr/bin/python
import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('Output2DatabaseV-03.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('Output2DatabaseV-03.py -i <inputfile> -o <outputfile>')
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
   barcount = 0
   for line in lines:
       count = 0
       #barcount = 0

       for character in line:
           print(barcount)
           if count == 0:
               lineTotal = character
               count = count + 1
           if count != 0:
               lineTotal = lineTotal + character
               count = count + 1
           if character == "|":
               barcount = barcount + 1
           elif barcount == 2:
               lineTotal = lineTotal + "\n"
               barcount = 0
       nextline = "> " + lineTotal
       outputfile.write(nextline)

   outputfile.close()



if __name__ == "__main__":
   main(sys.argv[1:])



