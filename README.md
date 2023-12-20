# LinkedIn Verification Script

This Python script is developed for partially verifying the association of LinkedIn account owners with email addresses. The script processes a CSV file containing email addresses and LinkedIn profile information and performs specific checks to validate name-email correlation.

## Table of Contents

1. [Script Functionality](#script-functionality)
2. [Prerequisites](#prerequisites)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Output](#output)

## Script Functionality

**Name-Email Correlation Check**: A substring check is performed to compare names with email addresses. The script checks if at least one word from the recipient's name is present in the email address.

## Prerequisites

- Python 3.8 installed on your machine.
- A CSV file with the following headers: 'First Name', 'Last Name', 'LinkedIn URL', 'Email Address', 'Company', 'Position'.

## Installation

1. Clone or download the script from the repository.
2. Ensure Python 3.8 is installed on your system.
3. Place your CSV file in the same directory as the script or specify the path in the script.

## Usage

1. Open the script in a Python editor or IDE.
2. Modify the `file_path` variable to the path of your CSV file.
3. Run the script. It will process the data and create a new file named "subject_for_review.csv" containing the results.

## Output

- The script will generate a file named "subject_for_review.csv".
- This file will include all the original data from the CSV file and an additional column 'Result' indicating 'Pass' or 'Fail' for each email based on the test criteria.
