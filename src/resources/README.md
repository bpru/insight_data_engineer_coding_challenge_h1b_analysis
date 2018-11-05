This folder has the following 2 files that contains necessary information for the data handeling step described in the Approach section of the main [`README.md`](../../README.md#approach) :

**`criteria.json`**:

```json
{
  "case_status": {
    "input_col_names": [
      "CASE_STATUS",
      "STATUS",
      "Approval_Status"
    ],
    "qualified_values": [
      "CERTIFIED"
    ]
  }
}
```
Each object has the following fields:

`input_col_names`: Stores a list of column names that might be encountered when dealing with data from differet years.

`qualified_values`: Stores all possible values that are considered "qualified". 

Currently, there is only one object with only one qualified value as shown above, but this structure allowsthe flexibility of adding more criteria and qualified values in the future. 


**`counting_targets.json`**:

```json
{
  "state": {
    "input_col_names": [
      "WORKSITE_STATE",
      "LCA_CASE_WORKLOC1_STATE",
      "State_1"
    ],
    "output_col_names": [
      "TOP_STATES",
      "NUMBER_CERTIFIED_APPLICATIONS",
      "PERCENTAGE"
    ],
    "top_k": 10,
    "output_file_name": "top_10_states.txt"
  },
  "occupation": {
    "input_col_names": [
      "SOC_NAME",
      "LCA_CASE_SOC_NAME",
      "Occupational_Title"
    ],
    "output_col_names": [
      "TOP_OCCUPATIONS",
      "NUMBER_CERTIFIED_APPLICATIONS",
      "PERCENTAGE"
    ],
    "top_k": 10,
    "output_file_name": "top_10_occupations.txt"
  }
}
```

Each object has the following fields:

`input_col_names`: Contains all possible column names when analyzing data from different years.

`output_col_names`: Column names required in the output file.

`top_k`: Number of top counting results included in the output file.

`output_file_name`: the name of output file for this particualr target.

As **`criteria.json`**, the structure of **`counting_targets.json`** also allows future expensions if  user needs to count more columns in the input data.