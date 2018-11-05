import csv
import sys
import pandas as pd
import re
from collections import Counter
from helpers import *

input_path = sys.argv[1]
OUTPUT_DIR = './output/'

# total number of certified applications
total = 0

# counts of all required fileds
counts = {target: Counter() for target in targets}

with open(input_path, mode='r') as f:
	# read input file
	reader = csv.reader(f, delimiter=';')

	# get column names (firt line of the input file) as a list
	columns = next(reader)

	# get indices of the interested column
	# criteria and targets are imported from helpers.py
	col_indices = get_col_indices(columns, criteria, targets)

	for row in reader:
		# check criteria
		if check_criteria(row, col_indices['criteria_cols'], criteria):
			total += 1
			count(row, col_indices['target_cols'], counts)

for target in targets:
	output_col_names = targets[target]['output_col_names']
	output_path = OUTPUT_DIR + targets[target]['output_file_name']
	counting = counts[target]
	top_k = targets[target]['top_k']
	save_file(output_col_names, counting, total, top_k, output_path)
	# with open(output_path, 'r') as f:
	# 	print(f.read())





	# tg_col_idx = get_col_idx(columns, TARGET_COLUMNS)

	# status_idx = tg_col_idx['CASE_STATUS']
	# state_idx = tg_col_idx['WORKSITE_STATE']
	# title_idx = tg_col_idx['SOC_NAME']
	
	# print(columns[status_idx], columns[state_idx], columns[title_idx])
	# print(type(reader))
# 	for row in reader:

# 		# print(row[visa_idx], row[status_idx], row[state_idx], row[title_idx])
# 		# if re.match(r'CERTIFIED', row[status_idx]):
# 		if row[status_idx] == 'CERTIFIED':
# 			total += 1
# 			states[row[state_idx]] += 1
# 			occupations[row[title_idx]] += 1

# with open(output_states_path, mode='w') as f:
# 	cnt_line = 0
# 	f.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')

# 	for state, cnt in sorted(states.items(), key=lambda x: (-x[1], x[0])):
# 		f.write('%s;%d;%.1f%%\n'%(state, cnt, cnt/total*100))
# 		cnt_line += 1
# 		if cnt_line == 10:
# 			break
# 		# print('%s;%d;%.1f%%\n'%(state, cnt, cnt/total*100))	

# with open(output_states_path, mode='r') as f:
# 	print(f.read())


# with open(output_occupations_path, mode='w') as f:
# 	cnt_line = 0
# 	f.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')

# 	for occupation, cnt in sorted(occupations.items(), key=lambda x: (-x[1], x[0])):
# 		f.write('%s;%d;%.1f%%\n'%(occupation, cnt, cnt/total*100))
# 		cnt_line += 1
# 		if cnt_line == 10:
# 			break
# 		# print('%s;%d;%.1f%%\n'%(state, cnt, cnt/total*100))

# with open(output_occupations_path, mode='r') as f:
# 	print(f.read())

		


