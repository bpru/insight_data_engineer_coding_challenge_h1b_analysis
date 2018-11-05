import json

# set invariants
RESOURCES_DIR = './src/resources/'
CRITERIA_PATH = RESOURCES_DIR + 'criteria.json'
COUNTING_TARGETS_PATH = RESOURCES_DIR + 'counting_targets.json'

CRITERIA = json.loads(open(CRITERIA_PATH).read())
TARGETS = json.loads(open(COUNTING_TARGETS_PATH).read())

def get_col_indices(columns, criteria, targets):
	"""Get indices of all required columns. 
	
	Args:
	    columns (list): list of all column names
	    criteria (dict): info of criteria for filtering data in the following structure
	    					{
	    						criterion_name_1: {
									'input_col_names': [possible column names...],
									'qualified_values': [qualified values...]
								},
								criterion_name_2: {
									'input_col_names': [possible column names...],
									'qualified_values': [qualified values...]
								},
								...
							}
	    targets (dict): info of targets to be conuted in the following structure
	    				{
							target_name_1: {
								'input_col_names': [possible coulmn names...],
								'output_col_names': [required output column names],
								'top_k': number of data to be stored in output file,
								'output_file_name': output file name
							}
							target_name_2: {
								'input_col_names': [possible coulmn names...],
								'output_col_names': [required output column names],
								'top_k': number of data to be stored in output file,
								'output_file_name': output file name
							},
							...
	    				}
	
	Returns:
	    dict: indices of all required columns in the following format:
	    	{
	    		'criteria_cols': 
	    			{
	    				criteria_name_1: index,
	    				criteria_name_2: index,
	    				...
	    			},
	    		'target_cols': 
	    			{
						target_name_1: index,
						target_name_2: index,
						...
	    			}
	    	}

	"""
	criteria_col_idx = {}
	target_col_idx = {}
	for idx, col in enumerate(columns):

		# get indices of criteria columns
		for criterion, info in criteria.items():

			# check if col equals to any of the candidate column names
			if col in info['input_col_names']:
				criteria_col_idx[criterion] = idx

		# get indices of target columns
		for target, info in targets.items():

			# check if col equals to any of the candidate column names
			if col in info['input_col_names']:
				target_col_idx[target] = idx
	return {'criteria_cols': criteria_col_idx, 'target_cols': target_col_idx}

def check_criteria(row, criteria_cols, criteria):
	"""Check to see if a row should be counted.
	
	Args:
	    row (list): a row of input file represented as a list
	    criteria_cols (dict): {
								criteria_name_1: index,
								criteria_name_2: index,
								...	
	    					   }
	    criteria (dict): {
							criteria_name_1: {
												'input_col_names': [possible column names...],
												'qualified_values': [qualified values...]
											  },
							criteria_name_2: {
												'input_col_names': [possible column names...],
												'qualified_values': [qualified values...]
											  },
							...
	    					}
	
	Returns:
	    boolean: True if this row should be counted, False otherwise.

	"""

	# go through every criterion to see if this row fulfill with all criteria
	for cri, idx in criteria_cols.items():
		if not row[idx] in criteria[cri]['qualified_values']:
			return False
	return True

def count(row, target_cols, counts):
	"""Perform counting for a given row
	
	Args:
	    row (list): a row of input file represented as a list
	    target_cols (dict): {
								target_name_1: index,
								target_name_2: index,
								...
	    					}
	    counts (dict): {
							target_name_1: { value_1: count, value_2: count, ... },
							target_name_2: { value_1: count, value_2: count, ... },
							...	
	    				}

	"""
	for tar, idx in target_cols.items():

		# increment counting
		counts[tar][row[idx]] += 1

def save_file(output_col_names, counting, total, top_k, output_path):
	"""Save counting results to output file in specified format
	
	Args:
	    output_col_names (string): required column names for output file
	    counting (Counter): counting result
	    total (int): total number of qualified applications for counting 
	    top_k (int): number of top countings to be stored in output file
	    output_path (string): path for output file
	"""
	with open(output_path, 'w') as f:

		# write column names
		f.write(';'.join(output_col_names)+'\n')

		# number of line written so far
		line_written = 0
		for item, cnt in sorted(counting.items(), key=lambda x: (-x[1], x[0])):

			# calculate and write counting data
			f.write('%s;%d;%.1f%%\n'%(item, cnt, cnt/total*100))
			line_written += 1

			# check if number of lines fulfills
			if line_written >= top_k:
				break


