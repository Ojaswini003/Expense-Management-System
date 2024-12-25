import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger=setup_logger('db_helper')


@contextmanager

def get_db_cursor(commit=False):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="expense_manager"


    )
    cursor=connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()

def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses_for_date called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s",(expense_date,))
        expenses=cursor.fetchall()
        return expenses

def delete_expenses_for_date(expense_date):
    logger.info(f"delete_expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def insert_expense(expense_date, amount, category, notes):
    logger.info(f"insert_expense called with : {expense_date}, amount:{amount}, category:{category}, notes:{notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )
    logger.info("Expense inserted successfully!")

def fetch_expense_summary(start_date, end_date):
    logger.info(f"fetch_expense_summary called with start : {start_date},end:{end_date}")

    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category, SUM(amount) as total
               FROM expenses WHERE expense_date
               BETWEEN %s and %s
               GROUP BY category;''',
            (start_date, end_date)
        )
        data = cursor.fetchall()
        return data
def fetch_monthly_expense_summary():
    logger.info(f"fetch_expense_summary_by_months")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT month(expense_date) as expense_month, 
               monthname(expense_date) as month_name,
               sum(amount) as total FROM expenses
               GROUP BY expense_month, month_name;
            '''
        )
        data = cursor.fetchall()
        return data

# if __name__ == "__main__":
#     expense = fetch_expenses_for_date("2024-08-01")
#     print(expense)
#     # delete_expenses_for_date("2024-08-25")
#     summary = fetch_expense_summary("2024-08-01", "2024-08-05")
#     for record in summary:
#         print(record)
# import mysql.connector
# from contextlib import contextmanager
# from logging_setup import setup_logger
#
# # Setup logger
# logger = setup_logger('db_helper')
#
# @contextmanager
# def get_db_cursor(commit=False):
#     connection = None
#     cursor = None
#     try:
#         # Create DB connection and cursor
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="root",
#             database="expense_manager"
#         )
#         cursor = connection.cursor(dictionary=True)
#         yield cursor  # Yield cursor to be used in the function calling this context manager
#         if commit:
#             connection.commit()
#     except mysql.connector.Error as e:
#         logger.error(f"Database error: {str(e)}")
#     finally:
#         # Ensure the cursor and connection are closed properly
#         if cursor:
#             cursor.close()
#         if connection:
#             connection.close()
#
# def fetch_expenses_for_date(expense_date):
#     logger.info(f"fetch_expenses_for_date called with {expense_date}")
#     try:
#         with get_db_cursor() as cursor:
#             cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
#             expenses = cursor.fetchall()
#             logger.info(f"Fetched {len(expenses)} expenses for date {expense_date}")
#             return expenses
#     except Exception as e:
#         logger.error(f"Error fetching expenses: {str(e)}")
#
# def delete_expenses_for_date(expense_date):
#     logger.info(f"delete_expenses_for_date called with {expense_date}")
#     try:
#         with get_db_cursor(commit=True) as cursor:
#             cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))
#             logger.info(f"Deleted expenses for date {expense_date}")
#     except Exception as e:
#         logger.error(f"Error deleting expenses: {str(e)}")
#
# def insert_expense(expense_date, amount, category, notes):
#     logger.info(f"insert_expense called with : {expense_date}, amount:{amount}, category:{category}, notes:{notes}")
#     try:
#         with get_db_cursor(commit=True) as cursor:
#             cursor.execute(
#                 "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
#                 (expense_date, amount, category, notes)
#             )
#         logger.info("Expense inserted successfully!")
#     except Exception as e:
#         logger.error(f"Failed to insert expense: {str(e)}")
#
# def fetch_expense_summary(start_date, end_date):
#     logger.info(f"fetch_expense_summary called with start: {start_date}, end: {end_date}")
#     try:
#         with get_db_cursor() as cursor:
#             cursor.execute(
#                 '''SELECT category, SUM(amount) as total
#                    FROM expenses WHERE expense_date
#                    BETWEEN %s and %s
#                    GROUP BY category;''',
#                 (start_date, end_date)
#             )
#             data = cursor.fetchall()
#             logger.info(f"Fetched {len(data)} summary entries")
#             return data
#     except Exception as e:
#         logger.error(f"Error fetching expense summary: {str(e)}")


