import random as rand
import numpy as np 

filename = 'ubmark-K-hilo.dat'
size = 1000;
int_size = 10;
src = []
ref = []

flag = 0

for x in range(0,int(size/int_size)):
    if (flag):
    	for y in range(0,int_size):
    		src.append(0)
    else:
    	for y in range(0,int_size):
    		src.append(rand.randint(9000, 10000))
    flag = not flag

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
file.write('// Data set for large 1000 HILO items.\n \n')
file.write('int size = ' + str(size) + ';\n \n')
file.write(form_src)
file.write(form_ref)

file.close()
