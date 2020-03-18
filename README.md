# Word_Blend
Programs to predict if a given word is a blend of two or more words from the english dictionary.
- Two different coding files have been implemented, one which is the original proposed system and the other an updation of the previous program:
Hamming Distance for word blend identification: kt.py
N-gram similarity for word blend identification: kt_update.py

- The development environment is python.

- The first program(hamming distance) makes use of the startswith() and endswith() methods of python to identify component words of a blend word.
The commands can have various parameters indicating from which index to check and till where to check.
Courtesy:https://www.geeksforgeeks.org/python-startswith-endswidth-function/

- The second program uses the package similarity and imports the ngram module. This program identifies the component words by comparing with index difference upto two values.
Courtesy:https://pythonhosted.org/ngram/ngram.html

- All three files namely candidate, dictionary and blends are read into a list, however blends file is only used for comparative analysis to check for correctness of the program.
The report details the comparison between the proposed and the updated system.
