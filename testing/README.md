# Run tests from command line

### unittest
```
python -m unittest test_unittest_calc  # run tests inside test_calc.py file
python -m unittest test_unittest_calc.py  # run tests inside test_calc.py file
python -m unittest -v test_unittest_calc  # run tests with verbose
python -m unittest discover  # run all test files found in the project
python -m unittest discover -v  # run all test files found in the project with verbose
```

### pytest
```
pytest  # run all tests inside the current folder and subdirectories
pytest -v  # run all tests with verbosity
pytest -q  # run all tests with less verbosity
pytest test_pytest_calc.py  # run tests inside the file
pytest testing/  # run all tests allocated inside testing folder
pytest -k "test_add"  # run test by keyword, in this case run the method test test_add()
pytest -v test_pytest_calc.py::TestCalc::test_multiply  # run a specific method
```

### doctest
```
python calculator.py  # execute docstring tests running the module as a script (don't display anything unless the test fails)
python calculator.py -v  # execute tests with verbose (in this case shows all tests)
# use testfile() method with a file to run tests
```