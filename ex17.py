from sys import argv
from os.path import exists

script, from_file, to_file = argv

print (f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?

# print (f"The input file is {len(indata)} bytes long")

print (f"Does the output file exists? {exists(to_file)}")
print (f"Ready, hit RETURN to continue, CTRL_C to abort.")
input()

out_file = open (to_file, 'w')
# out_file.write(indata)

print ("Alright, all done.")

out_file.close()
to_file.close()
