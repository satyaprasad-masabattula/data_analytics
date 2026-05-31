import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = 'http://localhost:8000'

def add_analytics_by_category_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start_Date:",datetime(2024,8,1))
    with col2:
        end_date = st.date_input('End_Date:',datetime(2024,8,5))

    if st.button('Get Analytics'):
        pay_load = {
            "start_date":start_date.strftime("%Y-%m-%d"),
            "end_date":end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics/",json=pay_load)
        data = response.json()

        df = pd.DataFrame({
            'Category':list(data.keys()),
            "Total": [value['total'] for category,value in data.items()],
            "Percentage":[value['percentage'] for category,value in data.items()],
        })
        df_sorted = df.sort_values(by='Percentage',ascending=False).reset_index(drop=True)

        st.title('Expense Breakdown By Category')
        st.bar_chart(data= df_sorted.set_index('Category')['Percentage'],width=700,height=400,use_container_width=True)
        st.table(df_sorted)
        # if(response.status_code ==  200):
        #     data = response.json()
        # else:
        #     st.error('Failed to get data')

