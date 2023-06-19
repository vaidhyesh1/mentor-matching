## Implementation of Matching Algorithm for mentors and mentees
##### Installation
`pip3 install -r requirements.txt`
##### Steps to run the code:

First run: 
`python3 saveInfo.py` to retrieve unassigned mentors and mentees from Mongo
Then run:
`python3 match.py` to run the matching algorithm and store the results locally
Finally run:
`python3 storeToDB.py` to push the generated matches back to mongo
