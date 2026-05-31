from backend import db_helper


def test_fetch_expense_for_date():
    expense = db_helper.fetch_expense_for_date('2024-08-15')

    assert len(expense)==1
    assert expense[0]['amount']==10.0
    assert expense[0]['category']=='Shopping'
    assert  expense[0]['notes']=='Bought potatoes'

def test_fetch_expense_for_date_no_valid():
    expense = db_helper.fetch_expense_for_date('2027-08-15')

    assert len(expense)==0


def test_fetch_expense_for_date_invalid_range():
    expense = db_helper.fetch_expense_summary('2027-08-15','2029-08-15')

    assert len(expense)==0

def test_fetch_expense_summary_by_month_invalid_year():
    expense = db_helper.fetch_expense_summary_by_month('2025')

    assert len(expense)==0
    
