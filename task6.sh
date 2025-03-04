#!/bin/bash

# Step 1: Activate the virtual environment
# Make sure to replace 'venv' with the name of your virtual environment folder (if it's different)
source venv/bin/activate

# Step 2: Run the test suite with pytest
pytest test_app.py

# Step 3: Check if the tests passed and return the corresponding exit code
if [ $? -eq 0 ]; then
    echo "Tests passed successfully!"
    exit 0  # Exit code 0 indicates success
else
    echo "Tests failed."
    exit 1  # Exit code 1 indicates failure
fi
