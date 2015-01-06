
import random

def gen_insults(file1, file2, file3):
	colA = make_list_from_file(file1)
	colB = make_list_from_file(file2)
	colC = make_list_from_file(file3)
	a = random.randrange(0, (len(colA)-1))
	b = random.randrange(0, (len(colB)-1))
	c = random.randrange(0, (len(colC)-1))
	return colA[a] + " " + colB[b] + " " + colC[c]

def make_list_from_file(source_file):
	source = open(source_file, 'r')
	return source.readlines()[0].split(',')

print(gen_insults('columnA.txt', 'columnB.txt', 'columnC.txt'))