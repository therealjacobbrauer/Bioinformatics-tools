# Bioinformatics-tools
This is a library to help in the development of bioinformatics libraries. 

Official documentation on NCBI BLAST database creation can be found here:

https://www.ncbi.nlm.nih.gov/books/NBK279688/

And the blast github page can be found here, with step by step instructions on how to make a database (db):

https://ncbi.github.io/magicblast/cook/blastdb.html

To run this python script: 
1. open a terminal
2. copy an input file and the python code into your CWD. 
3. type the following into your terminal:

python Output2DatabaseV-01.py -i <input_file> -o <output_file>

This will create a new file named what you refer to as the output file. 
If you name the output file the same thing as another file that already exsists in your CWD, 
then the program will write over that file. Please be careful to not write over other 
data that you need when running this script. 

______________________

If you copy into the ~/ncbi-blast-2.11.0+/bin folder two files:
1. Get_Output2.sh
2. Q9S.fasta (Your query, this was mine for the example)

Then you need to give you .sh script executable permissions. 
Make sure you are in root and type:

$chmod 755 Get_Output2.sh

or 

$chmod +x Get_Output2.sh

then

$./Get_Output2.sh 

And this will make a local blast database on your machine. 
