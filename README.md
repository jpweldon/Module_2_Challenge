# Module_2_Challenge

# Loan Qualifier Application

---

## Introduction:

The premise of this project is the scenario that I am progressing in a role as an application developer at a fintech lending startup. The lending software that I have built has been a big success for the company. As part of that success, I have been meeting a lot with the BizOps team to discuss creating additional useful features.

At a recent meeting, a new must-have feature request emerged. Specifically, BizOps wants to know if my software can prompt the user to save the qualifying loans as a new CSV file.

### User Story:

"As a user, I need the ability to save the qualifying loans to a CSV file so that I can share the results as a spreadsheet."

### Acceptance Criteria:

"Given that I am using the loan qualifier command-line interface (CLI), when I run the qualifier, then the tool should prompt the user to save the results as a CSV file."

"Given that there are no qualifying loans, when prompting a user to save a file, then the program should notify the user and exit."

"Given that I have a list of qualifying loans, when I am prompted to save the results, then I should be able to opt out of saving the file."

"Given that I have a list of qualifying loans, when I choose to save the loans, the tool should prompt for a file path to save the file."

"Given that I am using the loan qualifier CLI, when I choose to save the loans, then the tool should save the results as a CSV file."

---

## Technologies

This project leverages python 3.7.10 with the following modules:


* csv module

* pathlib module

* sys module

* fire library

* questionary library

---

## Installation Guide

Before running the application first install the following dependencies:

Install the fire library:

>'pip install fire'

Install the questionary library:

>'pip install questionary'

---

## Examples

---

## Usage

To use this program:

Clone the Module_2_Challenge repository from GitHub:

>'git clone https://github.com/jpweldon/Module_2_Challenge.git'

Change directories into the Starter_Code/qualifier directory:

>'cd Starter_Code/qualifier'

Run the app.py program:

>'python app.py'

---

If you want to run this program for your own data for different scenarios, simply follow the above steps with the exception to update or replace files in the Starter_Code/qualifier/data directory, Starter_Code/qualifier/qualifier/filters directory, and Starter_Code/qualifier/qualifier/utils directory to contain the data for your scenario(s) before running the program.

---

## Contributors

John P Weldon

Email: johnpweldon01@gmail.com

[LinkedIn:] (www.linkedin.com/in/john-weldon-333b0695)

---

## License

---
