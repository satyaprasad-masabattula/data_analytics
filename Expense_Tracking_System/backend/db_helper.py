import mysql.connector
from contextlib import contextmanager
from my_logger import set_my_looger

log = set_my_looger('db_helper','C:\satya\CodeBasics\projects\Expense_Tracking\logs\server.log')

@contextmanager
def get_db_cursor(commit=False):
    useName = 'root'
    password ='root'
    host = 'localhost'
    database = 'expense_manager'

    db_connection = mysql.connector.connect(user=useName,host=host,password=password,database=database)
    if(db_connection.is_connected()):
        cursor = db_connection.cursor(dictionary=True)
        yield cursor

        if(commit):
            db_connection.commit()
        cursor.close()
        db_connection.close()
    else:
        print('failed to connect db')

def fetch_expense_for_date(expnse_date):
    log.info(f'fetch_expense_for_date for date {expnse_date}')
    with get_db_cursor(commit=False) as cursor:
        cursor.execute("select * from expenses where expense_date = %s",(expnse_date,))
        expense = cursor.fetchall()
        return expense
    
def delete_expense_for_date(expnse_date):
    log.info(f'delete_expense_for_date for date {expnse_date}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("delete from expenses where expense_date = %s",(expnse_date,))

def insert_expense(expense_date,amount,category,notes):
    log.info(f'insert_expense for data {expense_date,amount,category,notes}')
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("insert into expenses (expense_date,amount,category,notes) values ( %s, %s, %s, %s)",(expense_date,amount,category,notes))

def fetch_expense_summary(start_date,end_date):
        log.info(f'fetch_expense_summary  date b/w {start_date} and {end_date}')
        with get_db_cursor(commit=False) as cursor:
            cursor.execute('''select category, sum(amount) as total_amount
                            from expenses 
                            where expense_date 
                            between %s and %s 
                            group by category;''',(start_date,end_date))
            expense = cursor.fetchall()
            return expense
        
def fetch_expense_summary_by_month():
        #log.info(f'fetch_expense_summary for all months for year {year_str}')
        log.info(f'fetch_expense_summary for all months')
        with get_db_cursor(commit=False) as cursor:
            cursor.execute('''select date_format(expense_date, '%b') as month,sum(amount) as total
                            from expenses 
                            group by month 
                            order by month;''')
            expense = cursor.fetchall()
            return expense
        
if __name__ == '__main__':
    expense_date = fetch_expense_for_date('2024-08-01')
    # print(expense_date)
    #insert_expense('2024-08-25',40,'Food','To taste bujji mixture')
    #delete_expense_for_date('2024-08-25')
    # summary=fetch_expense_summary('2024-08-01','2024-08-05')
    # for record in summary:
    #     print(record)

    summary = fetch_expense_summary_by_month()
    for record in summary:
         print(record)