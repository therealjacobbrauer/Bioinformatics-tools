#!/bin/bash

#this blasts againts the Q9S.fasta sequence
./blastp -db nr -query Q9S.fasta -out results_01.out -outfmt '6 sseqid sseq' -remote

# this is a python script that trims the output from above and makes it into a fasta file format that the makeblastdb can work with.  
python Output2DatabaseV-03.py -i results_01.fsa -o outV-04.fsa

#this makes a database using the outV-04.fsa as an input sequence
makeblastdb -in outV-04.fsa -blastdb_version 5 -title "Cookbook demo" -dbtype prot

echo "There are the following number of lines in the output blast search results file"
echo wc -l $results_01.out
echo "There are the following no. lines in the output cleaned fasta format file"
echo wc -l $outV-04.fsa
