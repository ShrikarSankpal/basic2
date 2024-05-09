def sum_numbers(input_file, output_file):
	with open(input_file,"r") as f:
		numbers = [int(line.strip()) for line in f]

	results = sum(numbers)

	with open(output_file,"w") as f:
		f.write(str(results))

if(__name__=="__main__"):
	input_file = "/home/user/projects/basic2/input/input_file.dat"
	output_file = "/home/user/projects/basic2/output/output_file.dat"

	sum_numbers(input_file, output_file)
