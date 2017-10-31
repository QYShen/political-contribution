# 1. General approach
Based on the requirement I recongnized "**recipient**" is the key that link both output files so my modeling is centralized on **Recipient** class. Will talk briefly later.
Based on the "consideration to keep in mind" section I noticed the importance of data sanitization so I model each transaction to a "Contribution" class. It has a #parse_contribution() factory method which does all the data sanitization. Valid attribute will be a concrete value while invalid one is None. If incoming transaction isn't valid at all, factory will produce None as returned value and in the processing code this entry will simply be ignored.
In "**Recipient**" class, the key method is **#receive_contribution()**, it process incoming transaction on the fly for both output file
Attributes:
```
self.txs_by_zipcode = {}  # {str:[]}
self.total_num_tx_by_zipcode = {}  # {str:int}
self.total_amount_by_zipcode = {}  # {str:int}
self.stats_by_zipcode = None  # str
```
is for medianval_by_zipcode.txt
While attributes:
```
self.txs_by_date = {}  # {int:[]}
self.total_num_tx_by_date = {}  # {date:int}
self.total_amount_by_date = {}  # {date:int}
```
is for medianval_by_date.txt

++There is emphasis on performance and time complexity, I tried my best to avoid unnecessary repetitive processing of old data.++

# 2. Dependencies
The only dependency is **pytest** for unit testing some building blocks.
As grader I'm sure you're already expert in it. To run some unit test please go to
`/src/unit_test`
To test each test file, in command line, invoke:
`$ pytest {TEST_FILE_NAME}`

# 3 Run Instruction
## 1. Just wanna see the result
One thing I want to emphasize is please run this project using python3.
This can be reflected by root directory's `run.sh` script.
`python3 ./src/find_political_donors.py ./input/itcont.txt ./output/medianvals_by_zip.txt ./output/medianvals_by_date.txt`

You can drop any file with `itcount.txt` name into `/input`, then in root directory invoke
`$ sh run.sh`
and you will get the 2 output files in `/output`

## 2. You have output files to check against
In `./insight_testsuite/tests` you can create a new test directory like `test_2`, create `/input` directory within it add input file named `itcount.txt`, put your expected output files in 
`./insight_testsuite/tests/test_2/output/medianvals_by_zip.txt` and `./insight_testsuite/tests/test_2/output/medianvals_by_date.txt`
in `./insight_testsuite` run `$ ./run_tests.sh`. All test cases in `./insight_testsuite/tests` will be run and checked.

## 3. Performance
For data from SEC website 2017-2018, "Contributions by Individuals"
ftp://ftp.fec.gov/FEC/2018/indiv18.zip
On a 2015 15 inch Macbook Pro, it consistantly takes around **5.5 minutes** to process the data, there are around 1.9 million records and input file size is about 900 MB. Have used "**cProfile**" package to profile and improve performance, this is so far the best I can do.