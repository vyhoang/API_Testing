# Python_API_Testing_Learning
This repo summarizes on what I learned from Python API Testing with BDD Framework.

 **File description:**
 
 - "utilities" folder contains files generalized and used for all tests
 - BDD behave framework in folder "features"
 - sql testing database at file "bookSQL_ForAPITest.sql"
 - csv testing data at file "loanData.csv"
 - requirements for Python package installation at file "requirements.txt"
 
 
**1. GitHub Authentication**:
 
Test gitHub API response with the given authentication data. 

**2. MySQL in Python:**
  
  Use package `mysql-connector-python` to connect and work with remote database.

**3. BDD framework in Python:**

Use package `behave` and Gherkin to test scenarios

 - Tests are written in natural language supported by Python code.

- Run behave in Terminal: 

    . test all features, run command: `behave features --no-capture`

    . test 1 feature, run command: `behave features/featureName.feature --no-capture`

    . environment.py: implements Hooks for the scenarios in the features
    
    . parameterization in test scenarios using Examples to test multiple data sets.
    
    . tags to run selected tests in framework like @smoke, @regression, @sprint15...
    
    . intergrate tags and hooks to generalize BDD code for all related tests

- Before running tests: change book data in bookAPI to make bookId data unique. 

- Allure reports for BDD test results: 

    . install package: `pip install allure-behave`
    
    . run command to create reports in json-formatted files: `behave --no-capture -f allure_behave.formatter:AllureFormatter -o AllureReportsName`

    .Download Allure Commandline Server: instructions from https://docs.qameta.io/allure/
    
    . In Powershell, run command to generate Allure report from json to html: `allure serve %allure_result_folder%`
 
 **4. CSV package**
 - Read data from csv file: reader()
 - Write data to csv file: writer()
 - Get value using index: index()
 
 **5. Web Scrapping with BeautifulSoup**
 - Extract list text from the website
 - Extract sub urls
 
