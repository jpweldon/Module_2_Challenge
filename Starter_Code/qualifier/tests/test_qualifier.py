# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import credit_score
from qualifier.filters import debt_to_income
from qualifier.filters import loan_to_value
from qualifier.filters import max_loan_size

# Test the save_csv Function
def test_save_csv():
    csvpath = Path('./data/output/qualifying_loans.csv')
    loans_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    fileio.save_csv(csvpath, loans_data)
    assert Path('./data/output/qualifying_loans.csv').exists()

# Test the calculate_monthly_debt_ratio Function
def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

# Test the calculate_loan_to_value_ratio Function
def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

# Test the filters
def test_filters():
    bank_data = fileio.load_csv(Path('./data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000

    monthly_debt_ratio = 0.375

    loan_to_value_ratio = 0.84

    # Run qualification filters
    bank_data_filtered = max_loan_size.filter_max_loan_size(loan, bank_data)
    bank_data_filtered = credit_score.filter_credit_score(current_credit_score, bank_data_filtered)
    bank_data_filtered = debt_to_income.filter_debt_to_income(monthly_debt_ratio, bank_data_filtered)
    bank_data_filtered = loan_to_value.filter_loan_to_value(loan_to_value_ratio, bank_data_filtered)

    assert len(bank_data_filtered) == 6

    # Test the save_csv Function with the Filtered Bank Data
    csvpath = Path('./data/output/qualifying_loans.csv')
    fileio.save_csv(csvpath, bank_data_filtered)
    assert Path('./data/output/qualifying_loans.csv').exists()
