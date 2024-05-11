import os

def sum_numbers(input_file, output_file):
	print("input_file: ",input_file)
	print("output file: ",output_file)
	with open(input_file,"r") as f:
		numbers = [int(line.strip()) for line in f]
		print("numbers: ",numbers)

	results = sum(numbers)
	print("results: ",results)

	with open(output_file,"w") as f:
		f.write(str(results))

if(__name__=="__main__"):
	input_file = "data/input_file.dat"
	output_file = "data/output_file.dat"
	input_file=os.path.abspath(input_file)
	output_file=os.path.abspath(output_file)

	sum_numbers(input_file, output_file)
