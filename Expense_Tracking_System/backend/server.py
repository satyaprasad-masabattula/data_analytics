from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel


class Expense(BaseModel):
    amount:float
    category:str
    notes:str

class ExpenseMonth(BaseModel):
    month:date
    total:float

class DateRange(BaseModel):
    start_date:date
    end_date:date

app = FastAPI()

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date:date):
    expense = db_helper.fetch_expense_for_date(expense_date)
    if expense is None:
        raise HTTPException(status_code=500,detail="Unable to retrive data due to internal issue")
    return expense



@app.post("/expenses/{expense_date}")
def get_add_update(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expense_for_date(expense_date)
    for record_expense in expenses:
        db_helper.insert_expense(expense_date,record_expense.amount,record_expense.category,record_expense.notes)
    return {'message':'sucessfully posted data'}

@app.post("/analytics/")
def get_analytics(date_range:DateRange):
    data = db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail="Unable to retrive data due to internal issue")
    total_expense = sum([row['total_amount'] for row in data])
    proceed_data = {}
    for row_data in data:
        percentage = round((row_data['total_amount']/total_expense)*100 if total_expense > 0 else 0,2)
        proceed_data[row_data['category']] = {'total':row_data['total_amount'],'percentage':percentage}
    return proceed_data
  
@app.get("/expensesbymonth/")
def get_expenses():
    expense = db_helper.fetch_expense_summary_by_month()
    if expense is None:
        raise HTTPException(status_code=500,detail="Unable to retrive data due to internal issue")
    return expense