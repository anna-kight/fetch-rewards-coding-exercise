# Fetch Rewards Coding Excercise - SDET

This is a selenium based project using python to preform required tasks and scenario for the Fetch Rewards Coding Excercise.  

## Set up:

### Install necessary programs:
This test is preformed in the [Google Chrome](https://www.google.com/chrome/) internet browser, this needs to be installed prior to running this test. 

This test also requires [python3](https://www.python.org/downloads/). This test was developed in python 3.8.5

### Create and activate a Vertual Environment:
Create and activate a python veriual environment to run the test in
```bashactivate
    python3 -m venv env
    source env/bin/
```

### Install necessary packages:
To install necessary python packages run the following from the command line
```bash
pip3 install -r requirements.txt
```

### Download the approprate chromedriver:
This repository includes the chromedriver version for google chrome Version 90.0.4430.93. I included this to avoid requiring other users to add the chromedriver to their system PATH environment variable.

If you are not usng version 90 of chrome you will need to replace the chromedriver file with the approprate [chromedriver](https://chromedriver.chromium.org/downloads) for your chrome version.

## Running the test:
To run the test from the command line run 
```bash
python3 -m pytest -s test_find_the_fake.py
```

When the test is finished you can deactivate your vertual environment by running 
```bash
deactivate
```
