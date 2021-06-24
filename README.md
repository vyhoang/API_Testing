# Python_API_Testing_Learning
This repo summarizes on what I learned from Python API Testing with BDD Framework.

**1. GitHub Authentication**: test gitHub API response with the given authentication data. 

**2. MySQL in Python:**  using library in mysql.connector to connect and work with database.

**3. BDD framework in Python:**
behave (use Cucumber components).

 - It uses tests written in natural language supported by Python.

- Run behave in Terminal: 

    . test all features, run command: `behave features --no-capture`

    . test 1 feature, run command: `behave features/bookAPI.feature --no-capture`

    . environment.py: implement Hooks for the scenarios in the features
    
    . Parameterization in test scenarios using Examples to test multiple data sets.
    
    . tags to run selected tests in framework like @smoke, @regression, @sprint15...
    
    . Intergrate tags and hooks to generalize BDD code for all related tests

- Before running tests: change book data in bookAPI to make bookId data unique. 

- Allure reports for BDD test results: 

    . install package: `pip install allure-behave`
    
    . run command to create reports in json-formatted files: `behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReportsName`

    .Download Allure Commandline Server: instructions from https://docs.qameta.io/allure/
    
    . In Powershell, run command to generate Allure report from json to html: `allure serve %allure_result_folder%`
 
  **4. CSV package**
 
 