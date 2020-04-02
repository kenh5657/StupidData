import random as rand
import numpy as np 

filename = 'ubmark-K-v-large.dat'
size = 3000;
src = []
ref = []

for x in range(0,size):
    src.append(rand.randint(0, 10000))

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
file.write('// Data set for large 1000 randomly sorted items.\n \n')
file.write('int size = ' + str(size) + ';\n \n')
file.write(form_src)
file.write(form_ref)

file.close()
