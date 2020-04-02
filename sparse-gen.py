import random as rand
import numpy as np 

filename = 'ubmark-K-sparse.dat'
size = 1000;
int_size  = 100;
int_s_size = 10;
src = []
ref = []


for x in range(0,int(size/int_size)):
    for y in range(0,int_s_size):
    	src.append(rand.randint(0, 10000))
    else:
    	for y in range(int_s_size,int_size):
    		src.append(0)

ref = sorted(src)

form_src = 'int src[] = { \n'
for elem in src:
	form_src = form_src + str(elem) +',\n'
form_src = form_src + '};\n\n'

form_ref = 'int ref[] = { \n'
for elem in ref:
	form_ref = form_ref + str(elem) +',\n'
form_ref = form_ref + '};'

open(filename, 'w').close()
file = open(filename,"w")
file.write('// Data set for large 1000 sparsely generated items.\n \n')
file.write('int size = ' + str(size) + ';\n \n')
file.write(form_src)
file.write(form_ref)

file.close()
