# Fetch Rewards Coding Excercise - SDET

This is a selenium based project using python to perform required tasks and scenario for the Fetch Rewards Coding Excercise.  

## Set up:

### Install necessary programs:
This test is performed in the [Google Chrome](https://www.google.com/chrome/) internet browser, this needs to be installed prior to running this test. 

This test also requires [python3](https://www.python.org/downloads/). This test was developed in python 3.8.5

### Create and activate a Virtual Environment:
Create and activate a python virtual environment to run the test in
```bashactivate
python3 -m venv env
source env/bin/
```
Note: if you are not using a virtual environment you will have to use python3 and pip3 commands rather than python and pip in later steps.

### Install necessary packages:
To install necessary python packages run the following from the command line
```bash
pip install -r requirements.txt
```

### Download the approprate chromedriver:
This repository includes the chromedriver version for google chrome Version 90.0.4430.93. I included this to avoid requiring other users to add the chromedriver to their system PATH environment variable.

If you are not usng version 90 of chrome you will need to replace the chromedriver file with the appropriate [chromedriver](https://chromedriver.chromium.org/downloads) for your chrome version.

## Running the test:
To run the test from the command line run 
```bash
python -m pytest -s test_find_the_fake.py
```

When the test is finished you can deactivate your virtual environment by running 
```bash
deactivate
```
