import sys
import os


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from fastapi import FastAPI,HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel



app=FastAPI()

class Expense (BaseModel):
    amount:float
    category:str
    notes:str

class DateRange(BaseModel):
        start_date: date
        end_date: date

@app.get("/expenses/{expense_date}",response_model=List[Expense])
def get_expenses(expense_date:date):
    # print(f"Received get_expense request: {expense_date}, type: {type(expense_date)}")
    expense=db_helper.fetch_expenses_for_date(expense_date)
    return expense
    # return {"date": expense_date, "expenses": 100}
@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date:date,expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount,expense.category,expense.notes)
    return{"message":"Expenses updated successfully"}

@app.post("/analytics/")
def get_analytics(date_range:DateRange):
    data=db_helper.fetch_expense_summary(date_range.start_date,date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500,detail="Failed to retrieve expense summary from data base" )
    total=sum(row['total'] for row in data)

    breakdown={}
    for row in data:
        percentage=(row['total']/total)*100 if total !=0 else 0
        breakdown[row['category']]={
            "total":row['total'],
            "percentage":percentage
        }
    return breakdown

@app.get("/monthly_summary/")
def get_analytics():
    monthly_summary = db_helper.fetch_monthly_expense_summary()
    if monthly_summary is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve monthly expense summary from the database.")

    return monthly_summary
