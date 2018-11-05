import json

RESOURCES_DIR = './src/resources/'
# RESOURCES_DIR = './resources/'
CRITERIA_PATH = RESOURCES_DIR + 'criteria.json'
COUNTING_TARGETS_PATH = RESOURCES_DIR + 'counting_targets.json'

criteria = json.loads(open(CRITERIA_PATH).read())
targets = json.loads(open(COUNTING_TARGETS_PATH).read())

def get_col_indices(columns, criteria, targets):
	criteria_col_idx = {}
	target_col_idx = {}
	for idx, col in enumerate(columns):
		for criterion, data in criteria.items():
			if col in data['input_col_names']:
				criteria_col_idx[criterion] = idx
		for target, data in targets.items():
			if col in data['input_col_names']:
				target_col_idx[target] = idx
	return {'criteria_cols': criteria_col_idx, 'target_cols': target_col_idx}

def check_criteria(row, criteria_cols, criteria):
	for cri, idx in criteria_cols.items():
		if not row[idx] in criteria[cri]['qualified_values']:
			return False
	return True

def count(row, target_cols, counts):
	for tar, idx in target_cols.items():
		counts[tar][row[idx]] += 1
	return

def save_file(output_col_names, counting, total, top_k, output_path):
	with open(output_path, 'w') as f:
		f.write(';'.join(output_col_names)+'\n')
		line_written = 0
		for item, cnt in sorted(counting.items(), key=lambda x: (-x[1], x[0])):
			f.write('%s;%d;%.1f%%\n'%(item, cnt, cnt/total*100))
			line_written += 1
			if line_written >= top_k:
				break

def filter(input, *criteria):
	return input in criteria


