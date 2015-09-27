import sys
import os
import csv
import string
import glob # Helps read from the existing folder.
import time

def main():
	files = glob.glob("*.csv")
	acceptable = { '.txt', '.csv' }
	dataFile = None

	while dataFile == None:
		outfile = input("Give name for output file: ").strip("'\"")
		try:
			dataFile = open(outfile, 'w+')
		except IOError as e:
			print("Try something like 'results.csv'.")

		if os.path.isdir(outfile):
			print("Give a filename, not a directory.")
			dataFile = None
		elif len(outfile) <= 4 or not(outfile[-4:] in acceptable):
			print("Invalid filename. Be sure to include file name and extension, e.g. 'results.csv'.")
			print("Aceptable file types: .txt, .csv")
			if not (dataFile == None):
				dataFile.close()
				os.remove(outfile)
			dataFile = None

	fixedColumns(files, outfile, dataFile)


def fixedColumns(files, outfile, dataFile):
	# t0 = time.time()
	readers = [csv.reader(open(file)) for file in files]
	data = [ [ row[1] for row in readers[i] ] for i in range(0, len(readers)) ]


	for j in range(0, len(data[0])):
		for i in range(0, len(data) - 1):
			try:
				dataFile.write(data[i][j].strip())
				dataFile.write(",")
			except IndexError:
				print("One of your data columns is longer than the others!")
		try:
			dataFile.write(data[len(data) - 1][j].strip())
			dataFile.write("\n")
		except IndexError:
			print("One of your data columns is longer than the others!")

	# t1 = time.time()
	# dataFile.write(str(t1 - t0))
	dataFile.close()
	print("Done! :)")

# def variableColumns():

# def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
# 	while True:
# 	    ok = input(prompt)
# 	    if ok in ('y', 'ye', 'yes'):
	        
# 	    if ok in ('n', 'no', 'nop', 'nope'):
# 	        return False
# 	    retries = retries - 1
# 	    if retries < 0:
# 	        raise OSError('uncooperative user')
# 	    print(complaint)


if __name__ == "__main__":
	main()	
