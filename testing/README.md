# Run tests from command line

### Unittest
```
python -m unittest test_unittest_calc  # run tests inside test_calc.py file
python -m unittest test_unittest_calc.py  # run tests inside test_calc.py file
python -m unittest -v test_unittest_calc  # run tests with verbose
python -m unittest discover  # run all test files found in the project
python -m unittest discover -v  # run all test files found in the project with verbose
```

### Pytest
```
pytest  # run all tests inside the current folder and subdirectories
pytest -v  # run all tests with verbosity
pytest -q  # run all tests with less verbosity
pytest test_pytest_calc.py  # run tests inside the file
pytest testing/  # run all tests allocated inside testing folder
pytest -k "test_add"  # run test by keyword, in this case run the method test test_add()
pytest -v test_pytest_calc.py::TestCalc::test_multiply  # run a specific method
```