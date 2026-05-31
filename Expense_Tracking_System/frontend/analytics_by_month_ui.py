import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = 'http://localhost:8000'

def add_analytics_by_month_tab():
    if st.button('Get Analytics By Month'):
        response = requests.get(f"{API_URL}/expensesbymonth/")
        data = response.json()
        df = pd.DataFrame({'month':rowdata['month'],'total':rowdata['total']} for rowdata in data)
        st.title('Expense Breakdown By Month')
        st.bar_chart(data= df.set_index('month')['total'],width=200,height=400,use_container_width=True)
        st.table(df)

