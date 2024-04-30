# ICTE_Electricty_Consuption_Cryptographic_Libraries

# Energy Monitor Database Integration

## Overview
This project involves running a script that monitors system energy usage and logs it to an InfluxDB database. It includes setting up the database and running tests with cryptographic libraries, followed by exporting analysis results to CSV files.

## Prerequisites
- Python 3 installed on your system.
- sudo privileges for running scripts.
- An account on InfluxDB along with a generated token, bucket, and organization.

## Configuration
1. **InfluxDB Setup:**
   - Sign up or log into InfluxDB and create a new database.
   - Generate a token, bucket, and organization name for accessing your database.
   - Update the `Energy_Monitor_to_DB.py` script with your InfluxDB credentials:
     ```python
     token = "your_token_here" # Replace with your token
     org = "your_org_name_here" # Replace with your organization name
     bucket = "your_bucket_name_here" # Replace with your bucket name
     ```

2. **Running the Script:**
   - Open your terminal.
   - Ensure you have sudo privileges and run the script with Python 3:
     ```bash
     sudo python3 Energy_Monitor_to_DB.py
     ```
   - This script should run continuously in the background to monitor and log data to your InfluxDB.

3. **Setting up Test Runner:**
   - Modify the `Test_runner.py` file:
     - Update `folder_path` with the project root directory where the cryptographic libraries are stored.
     - Add the path to your Python interpreter as an OS environment variable to enable automatic script execution.
     ```python
     import os
     os.environ['PYTHONPATH'] = "/path/to/your/python"
     ```

## Execution
- After setting up the `Test_runner.py` script, run it to execute all cryptographic library tests:
  ```bash
  python Test_runner.py
