# Continuous Integration(CI) for a simple Python application Using GitHub Actions

# GitHub Actions for Testing a Simple Math Operations Project

This repository contains a Python project demonstrating basic arithmetic operations and their corresponding test cases. The primary objective of this project is to illustrate the integration of GitHub Actions for continuous integration (CI) by automatically running tests upon changes to the codebase.

---

## Project Structure

The repository is organized as follows:

```
.
|-- src/
|   |-- maths_operations.py  # Contains the implementation of basic arithmetic operations
|
|-- tests/
|   |-- test_operations.py   # Contains test cases for the operations
|
|-- requirements.txt         # Lists project dependencies
|-- .github/
|   |-- workflows/
|       |-- python-tests.yml # GitHub Actions workflow file
```

### Key Files

1. **`src/maths_operations.py`**: Defines basic arithmetic functions such as addition, subtraction, multiplication, and division.
2. **`tests/test_operations.py`**: Contains test cases for the arithmetic functions using `pytest`.
3. **`requirements.txt`**: Specifies the required Python packages (`pytest` and others) to run the project and tests.
4. **`.github/workflows/python-tests.yml`**: The GitHub Actions workflow file for automating test execution.

---


## GitHub Actions Workflow

This project uses GitHub Actions to automate testing whenever there are changes pushed to the repository. The workflow file (`.github/workflows/python-tests.yml`) ensures continuous integration by running tests on each push or pull request.

### Workflow Overview

1. **Trigger**:
   - The workflow is triggered on every `push` or `pull_request` event.

2. **Environment**:
   - The workflow runs on `ubuntu-latest` virtual environments provided by GitHub.

3. **Steps**:
   - **Checkout the Code**: Uses `actions/checkout@v2` to fetch the code from the repository.
   - **Set Up Python**: Installs the desired Python version using `actions/setup-python@v4`.
   - **Install Dependencies**: Installs the required Python packages from `requirements.txt`.
   - **Run Tests**: Executes `pytest` to run the test cases.


---

## Running the Tests in GitHub Actions

Whenever code is pushed to the repository or a pull request is created:
1. GitHub Actions automatically triggers the workflow.
2. The workflow installs dependencies and runs the test cases.
3. Results are displayed in the **Actions** tab of the repository.

---


