import csv
import sys
import os
from collections import Counter
from helpers import *

def run(input_path, output_dir, criteria, targets):
	"""Main function to run the program.
	
	Args:
	    input_path (string): path of input file
	    output_dir (string): path of output directory
	    criteria (dict): see resources/criteria.json for structure
	    targets (dict): see resources/couting_targets.json for structure

	"""

	# total number of qualified applications for counting
	total = 0
	# use a dictionary of target_name: Counter to store counts of all required fileds
	counts = {target: Counter() for target in targets}
	with open(input_path, mode='r') as f:

		# read input csv file
		reader = csv.reader(f, delimiter=';')

		# save column names (firt line of the input file) as a list
		columns = next(reader)

		# get indices of the required columns for counting and store in a dictionary
		col_indices = get_col_indices(columns, criteria, targets)

		# get indices of columns for criteria and counting targets
		criteria_col_idx = col_indices['criteria_cols']
		target_col_idx = col_indices['target_cols']
		for row in reader:

			# check criteria
			if check_criteria(row, criteria_col_idx, criteria):

				# increment counting of qualifed applications
				total += 1

				# perform counting
				count(row, target_col_idx, counts)

	# save each counting result to its corresponding output file
	for target in targets:
		# get column names for output file
		output_col_names = targets[target]['output_col_names']

		# set output file path
		output_path = OUTPUT_DIR + targets[target]['output_file_name']

		# get counting data for this target
		counting = counts[target]

		# number of top results to save in the output file
		top_k = targets[target]['top_k']

		# save to output file
		save_file(output_col_names, counting, total, top_k, output_path)

# get input file path
INPUT_PATH = sys.argv[1]

# set output file directory
OUTPUT_DIR = os.path.dirname(INPUT_PATH) + '/../output/'

# run program
# CRITERIA and TARGETS are imported from helpers.py
run(INPUT_PATH, OUTPUT_DIR, CRITERIA, TARGETS)
