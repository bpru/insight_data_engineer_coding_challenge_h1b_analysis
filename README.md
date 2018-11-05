# Table of Contents
1. [Problem](README.md#problem)
2. [Approach](README.md#approach)
3. [Run Instructions](README.md#run-instructions)

# Problem

A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its [Office of Foreign Labor Certification Performance Data](https://www.foreignlaborcert.doleta.gov/performancedata.cfm#dis). But while there are ready-made reports for [2018](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2018/H-1B_Selected_Statistics_FY2018_Q4.pdf) and [2017](https://www.foreignlaborcert.doleta.gov/pdf/PerformanceData/2017/H-1B_Selected_Statistics_FY2017.pdf), the site doesn’t have them for past years. 

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: **Top 10 Occupations** and **Top 10 States** for **certified** visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the `input` directory, running the `run.sh` script should produce the results in the `output` folder without needing to change the code.

# Approach
### Repo directory structure
```
      ├── README.md 
      ├── run.sh
      ├── src
      │   ├──h1b_counting.py
      │   ├──helpers.py
      │   ├──resources
      │   |  ├──criteria.json
      │   |  └──counting_targets.json
      |   ├──unit_tests.py
      |   ├──columns.py
      |   └──run_test.sh
      |
      ├── input
      │   └──h1b_input.csv
      ├── output
      |   └── top_10_occupations.txt
      |   └── top_10_states.txt
      ├── insight_testsuite
          └── run_tests.sh
          └── tests
              └── test_1
              |   ├── input
              |   │   └── h1b_input.csv
              |   |__ output
              |   |   └── top_10_occupations.txt
              |   |   └── top_10_states.txt
              ├── your-own-test_1
                  ├── input
                  │   └── h1b_input.csv
                  |── output
                  |   |   └── top_10_occupations.txt
                  |   |   └── top_10_states.txt
```
Since the amount of input data could be very large, I take an approach that minimizes the need to load or store the entire data for processing. This approach can be explained in the following steps:

**Data Loading:** 

Load the input data using python's built-in csv library. This may take some time depends on the size of the input file.

**Data Handling:** 

As each row is read as a list of strings using python's csv.reader() method, this program searches only the first row for the index of interested columns. However, data from different years might use different column names for same type of information (e.g., `CASE_STATUS` and `STATUS` columns). Therefore, I included `src/resources/criteria.json` and `src/resources/counting_targets.json` to store all required information for getting correct columns for data filtering and data counting, respectively. Please see [`src/resources/README.md`](src/resources/README.md) for more details. The purpose of this step is to get indices of all required columns for later processing.

**Data Processing:**

After acquiring indices of all required columns, this program can get all required values in O(1) time, without the need to go through the entire row, which usually conatins dozens of columns. This program then iterates through all rows, selects qualified rows based on the criteria (in this case, `CASE_STATUS`, `STATUS`, or `Approval__Status` column equals to `"CERTIFIED"`), then stores the counts of targeted values (in this case, `WORKSITE_STATE` and `SOC_NAME` columns) into python built-in `Counter` objects. 

**Saving Output Files:**

Lastly, the statistics of values from tageted columns are calculated and written into corresponding output files. 

# Run Instructions
**Run Script**

Save the input file as `./input/h1b_input.csv` then run `./run.sh`.

**Run Unit Tests**

```
cd src
./run_test.sh 
```
