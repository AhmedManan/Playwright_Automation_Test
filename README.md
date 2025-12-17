# Playwright Automation Test

## Summary
In this repository we will conduct automation tests using Playwright, Python & Pytest. We will use POM(page object model) to conduct our automation test. We will also genatrate test reports on HTML.

---

## View Live Report

* **Allure Report:** [View Allure Report](https://ahmedmanan.github.io/Playwright_Automation_Test/reports/allure-report/index.html)
* **HTML Report:** [View HTML Report](https://ahmedmanan.github.io/Playwright_Automation_Test/reports/report.html)

## Table of Content
- [ View Live Report](#View-Live-Report)
- [Test Cases](#test-cases)
    - [Pytest Test List](#Pytest-Test-List)
    - [BDD Test List](#BDD-Test-List)
- [Additional Topics](#Additional-Topics)

## Project Setup

### Prerequisites
Before running the playwright tests, ensure you have the following installed on your system:

- Python (Installed in your device)
- Node ( Installed in your device)
- Java ( Installed in your device)
- A Code Editor ( PyCharm is recommended )

### Installation
- Clone this repository to your local machine.
- Install all prerequisites

To run the project in your local system, you need to install all the libraries listed in ``requirements.txt``
To install all the libraries at once, go to your project root directory and open terminal. Use the below command:

```bash
python -m pip install -r requirements.txt
```

Install the browsers Playwright needs:

```bash
playwright install
```
### Performing Tests with Pytest
The simplest way to run your tests is to call the pytest command with no arguments:
```aiignore
pytest
```

You can specify a file path or directory path after the pytest command. Example:
```aiignore
pytest tests/test_cases/test_01_login.py
```

## Test Cases

### Pytest Test List

| Serial | Test Script Name / Details                        | Status |
|--------|---------------------------------------------------|--------|
| 01     | Test OrangeHRM valid Login                        | ✔️     |
| 02     | Test OrangeHRM invalid Login                      | ✔️     |
| 03     | Test OrangeHRM dashboard                          | ✔️     |
| 04     | Test OrangeHRM dashboard sidebar navigation items | ✔️     |
| 05     | Test OrangeHRM dashboard sidebar navigation links | ✔️     |

### BDD Test List

| Serial | Test Script Name / Details | Status |
|--------|----------------------------|--------|
| 01     | Test OrangeHRM login       | ✔️     |


## Additional Topics

