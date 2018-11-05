from helpers import *
from columns import COLUMNS

def test_get_col_indices(name, columns, criteria, targets):
	print('Checking ' + name + ' ...')
	col_indicies = get_col_indices(columns, criteria, targets)
	criteria_cols_idx = col_indicies['criteria_cols']
	target_cols_idx = col_indicies['target_cols']
	assert columns[criteria_cols_idx['case_status']] in criteria['case_status']['input_col_names']
	assert columns[target_cols_idx['state']] in targets['state']['input_col_names']
	assert columns[target_cols_idx['occupation']] in targets['occupation']['input_col_names']
	print('Column name for case status:', columns[criteria_cols_idx['case_status']])
	print('Column name for work state:', columns[target_cols_idx['state']])
	print('Column name for occupation:', columns[target_cols_idx['occupation']])
	print('Pass!\n')

def test_check_criteria(criteria_cols, criteria):
	print('Checking check_criteria()...')
	row_1 = ['CERTIFIED']
	row_2 = ['CERTIFIED']
	row_3 = ['CERTIFIED']
	row_4 = ['CERTIFIED-WITHDRAWN']
	row_5 = ['DENIED']
	row_6 = ['DENIED']
	assert check_criteria(row_1, criteria_cols, criteria)
	assert check_criteria(row_2, criteria_cols, criteria)
	assert check_criteria(row_3, criteria_cols, criteria)
	assert not check_criteria(row_4, criteria_cols, criteria)
	assert not check_criteria(row_5, criteria_cols, criteria)
	assert not check_criteria(row_6, criteria_cols, criteria)
	print('Pass!')


print('Checking get_col_indices()...')
for name, columns in sorted(COLUMNS.items(), key=lambda x: x[0]):
	test_get_col_indices(name, columns, CRITERIA, TARGETS)

test_check_criteria({'case_status': 0}, CRITERIA)
